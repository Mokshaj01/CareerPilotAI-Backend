
from fastapi import APIRouter, HTTPException

from app.data.job_taxonomy import (
    PROFESSIONAL_FIELDS,
    SUBFIELDS_BY_FIELD,
    CANONICAL_ROLES,
    TAXONOMY_VERSION,
    get_subfields_by_field,
)

router = APIRouter()


@router.get("/fields")
async def get_professional_fields():
    """Return all available professional fields."""
    return {
        "taxonomy_version": TAXONOMY_VERSION,
        "total": len(PROFESSIONAL_FIELDS),
        "fields": PROFESSIONAL_FIELDS,
    }


@router.get("/fields/{field_id}/subfields")
async def get_subfields(field_id: str):
    """Return subfields belonging to a professional field."""

    field = next(
        (item for item in PROFESSIONAL_FIELDS if item["id"] == field_id),
        None,
    )

    if field is None:
        raise HTTPException(
            status_code=404,
            detail=f"Professional field '{field_id}' not found.",
        )

    subfields = get_subfields_by_field(field_id)

    return {
        "taxonomy_version": TAXONOMY_VERSION,
        "field_id": field_id,
        "field_name": field["name"],
        "total": len(subfields),
        "subfields": subfields,
    }


@router.get("/fields/{field_id}/roles")
async def get_roles_by_field(field_id: str):
    """Return active canonical roles belonging to a professional field."""

    field = next(
        (item for item in PROFESSIONAL_FIELDS if item["id"] == field_id),
        None,
    )

    if field is None:
        raise HTTPException(
            status_code=404,
            detail=f"Professional field '{field_id}' not found.",
        )

    roles = [
        role for role in CANONICAL_ROLES
        if role["professional_field_id"] == field_id
        and role.get("is_active", False)
    ]

    return {
        "taxonomy_version": TAXONOMY_VERSION,
        "field_id": field_id,
        "field_name": field["name"],
        "total": len(roles),
        "roles": roles,
    }


@router.get("/fields/{field_id}/subfields/{subfield_id}/roles")
async def get_roles_by_subfield(field_id: str, subfield_id: str):
    """Return active canonical roles belonging to a specific subfield."""

    field = next(
        (item for item in PROFESSIONAL_FIELDS if item["id"] == field_id),
        None,
    )

    if field is None:
        raise HTTPException(
            status_code=404,
            detail=f"Professional field '{field_id}' not found.",
        )

    subfields = SUBFIELDS_BY_FIELD.get(field_id, [])

    subfield = next(
        (item for item in subfields if item["id"] == subfield_id),
        None,
    )

    if subfield is None:
        raise HTTPException(
            status_code=404,
            detail=f"Subfield '{subfield_id}' not found in '{field_id}'.",
        )

    roles = [
        role for role in CANONICAL_ROLES
        if role["professional_field_id"] == field_id
        and role["subfield_id"] == subfield_id
        and role.get("is_active", False)
    ]

    return {
        "taxonomy_version": TAXONOMY_VERSION,
        "field_id": field_id,
        "field_name": field["name"],
        "subfield_id": subfield_id,
        "subfield_name": subfield["name"],
        "total": len(roles),
        "roles": roles,
    }


@router.get("/roles/{role_id}")
async def get_canonical_role(role_id: str):
    """Return one active canonical role by its ID."""

    role = next(
        (
            item for item in CANONICAL_ROLES
            if item["id"] == role_id and item.get("is_active", False)
        ),
        None,
    )

    if role is None:
        raise HTTPException(
            status_code=404,
            detail=f"Active canonical role '{role_id}' not found.",
        )

    return {
        "taxonomy_version": TAXONOMY_VERSION,
        "role": role,
    }
