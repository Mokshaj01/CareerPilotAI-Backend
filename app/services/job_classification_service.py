import re
import unicodedata
from typing import Any, Dict, Optional, List, Tuple

from app.data.job_taxonomy import (
    CANONICAL_ROLES,
    ROLE_ALIASES,
    ROLE_CROSS_FIELD_MAPPINGS,
)

WORK_DESCRIPTORS = {
    "remote",
    "hybrid",
    "onsite",
    "on site",
    "work from home",
    "wfh",
}

SENIORITY_DESCRIPTORS = {
    "senior",
    "junior",
    "lead",
    "principal",
    "associate",
    "entry level",
    "mid level",
    "mid senior",
    "staff",
}


def normalize_role_text(value: str) -> str:
    """Normalize role names, IDs, and aliases."""
    if not value:
        return ""

    value = unicodedata.normalize("NFKC", str(value))
    value = value.casefold()
    value = value.replace("&", " and ")
    value = value.replace("_", " ")
    value = re.sub(r"[^a-z0-9]+", " ", value)

    return " ".join(value.split())


def _build_role_indexes():
    """Build lookup indexes using active canonical roles and aliases."""
    roles_by_id = {}
    title_lookup = {}
    ambiguous_terms = set()

    for role in CANONICAL_ROLES:
        if not role.get("is_active", True):
            continue

        role_id = role.get("id")
        role_name = role.get("name")

        if not role_id or not role_name:
            continue

        roles_by_id[role_id] = role

        for term in (
            normalize_role_text(role_name),
            normalize_role_text(role_id),
        ):
            if not term:
                continue

            existing = title_lookup.get(term)

            if existing and existing["id"] != role_id:
                ambiguous_terms.add(term)
            else:
                title_lookup[term] = role

    for alias_entry in ROLE_ALIASES:
        if not alias_entry.get("is_active", True):
            continue

        alias = alias_entry.get("alias")
        canonical_role_id = alias_entry.get("canonical_role_id")
        role = roles_by_id.get(canonical_role_id)

        if not alias or not role:
            continue

        term = normalize_role_text(alias)

        if not term:
            continue

        existing = title_lookup.get(term)

        if existing and existing["id"] != canonical_role_id:
            ambiguous_terms.add(term)
        else:
            title_lookup[term] = role

    return roles_by_id, title_lookup, ambiguous_terms


ROLES_BY_ID, ROLE_LOOKUP, AMBIGUOUS_TERMS = _build_role_indexes()


def _remove_work_descriptors(title: str) -> str:
    """Remove known work arrangement descriptors at title boundaries."""
    words = title.split()

    while words and words[0] in WORK_DESCRIPTORS:
        words.pop(0)

    while words and words[-1] in WORK_DESCRIPTORS:
        words.pop()

    return " ".join(words)


def _remove_seniority_descriptors(title: str) -> str:
    """Remove known seniority descriptors at title boundaries."""
    words = title.split()

    changed = True

    while words and changed:
        changed = False

        for descriptor in sorted(
            SENIORITY_DESCRIPTORS,
            key=len,
            reverse=True,
        ):
            descriptor_words = descriptor.split()
            count = len(descriptor_words)

            if words[:count] == descriptor_words:
                words = words[count:]
                changed = True
                break

            if words[-count:] == descriptor_words:
                words = words[:-count]
                changed = True
                break

    return " ".join(words)


def _get_title_candidates(title: str) -> List[Tuple[str, str]]:
    """Generate progressively normalized title candidates."""
    candidates = []

    work_cleaned = _remove_work_descriptors(title)

    if work_cleaned and work_cleaned != title:
        candidates.append(
            (work_cleaned, "normalized_work_descriptor")
        )

    seniority_cleaned = _remove_seniority_descriptors(work_cleaned)

    if seniority_cleaned and seniority_cleaned != work_cleaned:
        candidates.append(
            (seniority_cleaned, "normalized_seniority")
        )

    return candidates


def _resolve_exact_title(title: str):
    """Resolve a complete canonical name, ID, or alias."""
    if title in AMBIGUOUS_TERMS:
        return None, "ambiguous"

    role = ROLE_LOOKUP.get(title)

    if not role:
        return None, None

    if title == normalize_role_text(role["name"]):
        return role, "canonical_name"

    if title == normalize_role_text(role["id"]):
        return role, "canonical_id"

    return role, "alias"


def _find_contiguous_matches(title: str) -> List[Dict[str, Any]]:
    """
    Find role phrases appearing contiguously in the title.

    Words are never skipped. This prevents unrelated phrases from
    accidentally being combined into a role match.
    """
    title_words = title.split()
    matches_by_role = {}

    for term, role in ROLE_LOOKUP.items():
        if term in AMBIGUOUS_TERMS:
            continue

        term_words = term.split()
        size = len(term_words)

        if not size or size > len(title_words):
            continue

        for start in range(len(title_words) - size + 1):
            if title_words[start:start + size] != term_words:
                continue

            candidate = {
                "role": role,
                "role_id": role["id"],
                "matched_term": term,
                "match_type": "partial_phrase",
                "start": start,
                "end": start + size,
                "coordinated": False,
            }

            existing = matches_by_role.get(role["id"])

            if existing is None or size > (
                existing["end"] - existing["start"]
            ):
                matches_by_role[role["id"]] = candidate

    return list(matches_by_role.values())


def _find_coordinated_matches(title: str) -> List[Dict[str, Any]]:
    """
    Detect shared-head titles such as:
        Python and Java Developer
        Java and Python Developer

    The shared job-role ending is applied to the preceding modifier.
    """
    words = title.split()
    results = []

    for index, word in enumerate(words):
        if word != "and" or index == 0 or index == len(words) - 1:
            continue

        left_words = words[:index]
        right_words = words[index + 1:]

        # Find a recognized role phrase ending the right-hand side.
        for term, right_role in ROLE_LOOKUP.items():
            if term in AMBIGUOUS_TERMS:
                continue

            term_words = term.split()
            term_size = len(term_words)

            if len(right_words) < term_size:
                continue

            if right_words[-term_size:] != term_words:
                continue

            # Try the shared final one, two, or three words.
            for suffix_size in range(
                1, min(3, term_size) + 1
            ):
                shared_suffix = term_words[-suffix_size:]

                left_candidate = " ".join(
                    left_words + shared_suffix
                )

                left_role = ROLE_LOOKUP.get(left_candidate)

                if not left_role:
                    continue

                if left_candidate in AMBIGUOUS_TERMS:
                    continue

                results.append({
                    "role": left_role,
                    "role_id": left_role["id"],
                    "matched_term": left_candidate,
                    "match_type": "coordinated_phrase",
                    "coordinated": True,
                })

                break

    # Remove duplicate coordinated roles.
    unique = {}

    for candidate in results:
        unique[candidate["role_id"]] = candidate

    return list(unique.values())


def _remove_nested_matches(
    matches: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Prefer a more specific contiguous role phrase over a shorter
    role phrase contained entirely inside it.

    Coordinated matches are retained independently.
    """
    filtered = []

    for candidate in matches:
        if candidate.get("coordinated"):
            filtered.append(candidate)
            continue

        nested = False

        for other in matches:
            if other["role_id"] == candidate["role_id"]:
                continue

            if other.get("coordinated"):
                continue

            contains_candidate = (
                other["start"] <= candidate["start"]
                and other["end"] >= candidate["end"]
                and (
                    other["start"] < candidate["start"]
                    or other["end"] > candidate["end"]
                )
            )

            if contains_candidate:
                nested = True
                break

        if not nested:
            filtered.append(candidate)

    return filtered


# ------------------------------------------------------------
# Order-independent partial role matching
# ------------------------------------------------------------

UNORDERED_GENERIC_ROLE_WORDS = {
    "engineer",
    "analyst",
    "designer",
    "developer",
    "consultant",
    "professional",
    "lead",
    "staff",
    "nurse",
}

UNORDERED_IGNORED_TITLE_WORDS = {
    "professional",
    "position",
    "job",
    "role",
}


def _prepare_unordered_tokens(value: str) -> List[str]:
    """
    Prepare tokens for order-independent role matching.

    Preserve role-defining words and apply only controlled
    equivalences.
    """
    tokens = normalize_role_text(value).split()

    tokens = [
        "analyst" if token == "analysis" else token
        for token in tokens
    ]

    normalized_tokens = []
    index = 0

    while index < len(tokens):
        # CAD Design is treated as one concept.
        if tokens[index:index + 2] == ["cad", "design"]:
            normalized_tokens.append("cad")
            index += 2
            continue

        # Computer Aided Design is treated as CAD.
        if tokens[index:index + 3] == [
            "computer", "aided", "design"
        ]:
            normalized_tokens.append("cad")
            index += 3
            continue

        normalized_tokens.append(tokens[index])
        index += 1

    # Avoid counting the same word more than once.
    return list(dict.fromkeys(normalized_tokens))


def _unordered_tokens_match(left: str, right: str) -> bool:
    """Apply controlled equivalence between role-title words."""
    if left == right:
        return True

    return {left, right} == {"engineer", "engineering"}


def _unordered_token_weight(token: str) -> float:
    """Downweight generic role words without removing them."""
    if token in UNORDERED_GENERIC_ROLE_WORDS:
        return 0.35

    return 1.0


def _build_unordered_phrase_index():
    """
    Build candidate phrases from existing canonical names,
    role IDs, and aliases.
    """
    phrases_by_role = {}

    for term, role in ROLE_LOOKUP.items():
        if term in AMBIGUOUS_TERMS:
            continue

        tokens = _prepare_unordered_tokens(term)

        if len(tokens) < 2:
            continue

        phrases_by_role.setdefault(role["id"], []).append({
            "role": role,
            "term": term,
            "tokens": tokens,
        })

    return phrases_by_role


UNORDERED_PHRASES_BY_ROLE = _build_unordered_phrase_index()


def _rank_unordered_candidates(title: str) -> List[Dict[str, Any]]:
    """
    Rank canonical roles by weighted, order-independent
    token overlap with the job title.
    """
    normalized = normalize_role_text(title)
    normalized = _remove_work_descriptors(normalized)
    normalized = _remove_seniority_descriptors(normalized)

    title_tokens = [
        token
        for token in _prepare_unordered_tokens(normalized)
        if token not in UNORDERED_IGNORED_TITLE_WORDS
    ]

    if not title_tokens:
        return []

    title_weight = sum(
        _unordered_token_weight(token)
        for token in title_tokens
    )

    ranked = []

    for role_id, phrases in UNORDERED_PHRASES_BY_ROLE.items():
        best = None

        for phrase in phrases:
            candidate_tokens = phrase["tokens"]

            used_title_tokens = set()
            matched_candidate_tokens = []

            # Each candidate word can match at most one
            # corresponding title word.
            for candidate_token in candidate_tokens:
                match = next(
                    (
                        title_token
                        for title_token in title_tokens
                        if (
                            title_token not in used_title_tokens
                            and _unordered_tokens_match(
                                candidate_token,
                                title_token,
                            )
                        )
                    ),
                    None,
                )

                if match is not None:
                    used_title_tokens.add(match)
                    matched_candidate_tokens.append(
                        candidate_token
                    )

            candidate_weight = sum(
                _unordered_token_weight(token)
                for token in candidate_tokens
            )

            matched_candidate_weight = sum(
                _unordered_token_weight(token)
                for token in matched_candidate_tokens
            )

            matched_title_weight = sum(
                _unordered_token_weight(token)
                for token in used_title_tokens
            )

            coverage = (
                matched_candidate_weight / candidate_weight
                if candidate_weight else 0.0
            )

            precision = (
                matched_title_weight / title_weight
                if title_weight else 0.0
            )

            score = (
                0.70 * coverage
                + 0.30 * precision
            )

            result = {
                "role": phrase["role"],
                "role_id": role_id,
                "matched_term": phrase["term"],
                "matched_tokens": matched_candidate_tokens,
                "coverage": coverage,
                "precision": precision,
                "score": score,
            }

            if best is None or score > best["score"]:
                best = result

        if best:
            ranked.append(best)

    ranked.sort(
        key=lambda item: (
            item["score"],
            item["coverage"],
            item["precision"],
        ),
        reverse=True,
    )

    return ranked


def _find_unordered_match(
    title: str,
) -> Tuple[str, Optional[Dict[str, Any]]]:
    """
    Find a sufficiently strong order-independent role match.

    Return unmatched, matched, or ambiguous.
    """
    ranked = _rank_unordered_candidates(title)

    accepted = [
        item
        for item in ranked
        if (
            item["coverage"] >= 0.90
            and item["precision"] >= 0.55
        )
    ]

    if not accepted:
        return "unmatched", None

    best = accepted[0]

    runner_up = next(
        (
            item
            for item in accepted[1:]
            if item["role_id"] != best["role_id"]
        ),
        None,
    )

    # Avoid arbitrary selection when two different roles
    # have similarly strong evidence.
    if (
        runner_up
        and best["score"] - runner_up["score"] < 0.08
    ):
        return "ambiguous", None

    return "matched", {
        "role": best["role"],
        "role_id": best["role_id"],
        "matched_term": best["matched_term"],
        "match_type": "partial_unordered",
        "coordinated": False,
        "coverage": best["coverage"],
        "precision": best["precision"],
        "score": best["score"],
    }


def _build_result(
    status: str,
    roles: Optional[List[Dict[str, Any]]] = None,
    match_type: Optional[str] = None,
    matched_term: Optional[str] = None,
    role_matches: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """Build a result with primary and additional professional fields."""
    roles = roles or []
    role_matches = role_matches or []

    role_ids = sorted({
        role["id"] for role in roles
    })

    primary_fields = {
        role["professional_field_id"]
        for role in roles
        if role.get("professional_field_id")
    }

    subfields = {
        role["subfield_id"]
        for role in roles
        if role.get("subfield_id")
    }

    shared_field = (
        next(iter(primary_fields))
        if len(primary_fields) == 1 and len(primary_fields) == len({
            role.get("professional_field_id") for role in roles
        })
        else None
    )

    shared_subfield = (
        next(iter(subfields))
        if len(subfields) == 1 and shared_field is not None
        and all(role.get("subfield_id") for role in roles)
        else None
    )

    matches_by_id = {
        candidate.get("role_id"): candidate
        for candidate in role_matches
        if candidate.get("role_id")
    }

    role_details = []
    all_additional_fields = set()

    for role in roles:
        role_id = role["id"]
        candidate = matches_by_id.get(role_id, {})

        role_match_type = candidate.get("match_type")

        if not role_match_type:
            role_match_type = (
                "partial_phrase"
                if role_matches
                else match_type
            )

        role_primary_field = role.get("professional_field_id")

        additional_fields = sorted({
            field_id
            for field_id in ROLE_CROSS_FIELD_MAPPINGS.get(
                role_id, []
            )
            if field_id and field_id != role_primary_field
        })

        all_additional_fields.update(additional_fields)

        role_details.append({
            "canonical_role_id": role_id,
            "canonical_role_name": role.get("name"),
            "professional_field_id": role_primary_field,
            "subfield_id": role.get("subfield_id"),
            "additional_professional_field_ids": additional_fields,
            "match_type": role_match_type,
            "matched_term": candidate.get(
                "matched_term",
                matched_term,
            ),
        })

    # Do not report a field as additional if it is already
    # represented as a primary field by another matched role.
    overall_additional_fields = (
        all_additional_fields - primary_fields
    )

    all_fields = primary_fields | all_additional_fields

    return {
        "status": status,
        "professional_field_id": shared_field,
        "subfield_id": shared_subfield,
        "primary_professional_field_ids": sorted(primary_fields),
        "additional_professional_field_ids": sorted(
            overall_additional_fields
        ),
        "all_professional_field_ids": sorted(all_fields),
        "canonical_role_id": (
            role_ids[0] if len(role_ids) == 1 else None
        ),
        "candidate_role_ids": role_ids,
        "match_type": match_type,
        "matched_term": matched_term,
        "roles": role_details,
    }

def classify_job(
    title: Optional[str],
    description: Optional[str] = None,
    requirements: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Classify a job title.

    Exact canonical names and aliases take priority over partial
    matching. Multiple confidently identified roles are retained.

    Description and requirements are reserved for future contextual
    classification and do not independently create role matches.
    """
    normalized_title = normalize_role_text(title or "")

    if not normalized_title:
        return _build_result("unmatched")

    # 1. Exact full-title matching.
    role, match_type = _resolve_exact_title(normalized_title)

    if match_type == "ambiguous":
        return _build_result(
            "ambiguous",
            matched_term=normalized_title,
        )

    if role:
        return _build_result(
            "matched",
            [role],
            match_type,
            title,
        )

    # 2. Try work-descriptor and seniority normalization.
    for candidate, normalization_type in _get_title_candidates(
        normalized_title
    ):
        role, match_type = _resolve_exact_title(candidate)

        if match_type == "ambiguous":
            return _build_result(
                "ambiguous",
                matched_term=candidate,
            )

        if role:
            return _build_result(
                "matched",
                [role],
                normalization_type,
                title,
            )

    # 3. Remove work and seniority descriptors for the
    #    original partial-matching attempt.
    work_cleaned_title = _remove_work_descriptors(normalized_title)

    partial_title = _remove_seniority_descriptors(
        work_cleaned_title
    )

    # 4. First attempt: preserve the existing matching behavior.
    matches = []

    if partial_title:
        matches = _find_contiguous_matches(partial_title)

        coordinated = _find_coordinated_matches(partial_title)

        for candidate in coordinated:
            if not any(
                existing["role_id"] == candidate["role_id"]
                for existing in matches
            ):
                matches.append(candidate)

    # 5. Fallback: retry without removing seniority descriptors.
    #    This runs only when the original attempt finds no roles.
    if not matches and work_cleaned_title:
        partial_title = work_cleaned_title

        matches = _find_contiguous_matches(partial_title)

        coordinated = _find_coordinated_matches(partial_title)

        for candidate in coordinated:
            if not any(
                existing["role_id"] == candidate["role_id"]
                for existing in matches
            ):
                matches.append(candidate)


    # 6. Final fallback: order-independent partial matching.
    #    This runs only when all existing matching stages fail.
    if not matches:
        unordered_status, unordered_match = (
            _find_unordered_match(normalized_title)
        )

        if unordered_status == "ambiguous":
            return _build_result(
                "ambiguous",
                match_type="partial_unordered",
                matched_term=title,
            )

        if unordered_match:
            matches = [unordered_match]

    if not matches:
        return _build_result("unmatched")

    # 6. Remove less-specific nested phrase matches.
    matches = _remove_nested_matches(matches)

    roles_by_id = {
        candidate["role_id"]: candidate["role"]
        for candidate in matches
    }

    roles = list(roles_by_id.values())

    if len(roles) == 1:
        candidate = matches[0]

        result_match_type = candidate.get(
            "match_type",
            "partial_phrase",
        )

        return _build_result(
            "matched",
            roles,
            result_match_type,
            candidate["matched_term"],
            role_matches=matches,
        )

    return _build_result(
        "multi_role",
        roles,
        "multiple_role_phrases",
        title,
        role_matches=matches,
    )


def get_classification_index_stats() -> Dict[str, int]:
    """Return classification index statistics."""
    return {
        "active_canonical_roles": len(ROLES_BY_ID),
        "lookup_terms": len(ROLE_LOOKUP),
        "ambiguous_terms": len(AMBIGUOUS_TERMS),
    }
