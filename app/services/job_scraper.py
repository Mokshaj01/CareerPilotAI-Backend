import logging
from datetime import datetime, timedelta
from typing import List, Optional
from sqlalchemy.orm import Session
import pandas as pd
import re

from app.models import Job, Company, JobRoleAssociation
from app.database import SessionLocal
from app.services.job_classification_service import classify_job

logger = logging.getLogger(__name__)

class JobSpyScraper:
    def __init__(self):
        self.supported_sites = ["linkedin", "indeed", "glassdoor", "google"]
    
    @staticmethod
    def clean_str(val):
        """Safely strip and lower-case a value if it's a string."""
        if isinstance(val, str):
            return val.strip()
        return ""
    
    @staticmethod
    def safe_string(val):
        """Returns string, or empty string if NaN or None."""
        if pd.isna(val) or val is None:
            return ""
        return str(val)
    
    def clean_salary(self, min_amount, max_amount, currency=None, interval=None):
        """Clean salary amounts, ensure they are int or None, assign currency and period."""
        clean_currency = self.safe_string(currency) or "USD"
        clean_period = "year"
        if interval:
            interval_lower = str(interval).lower()
            if "hour" in interval_lower:
                clean_period = "hour"
            elif "month" in interval_lower:
                clean_period = "month"
            elif "year" in interval_lower or "annual" in interval_lower:
                clean_period = "year"
        try:
            clean_min = int(float(min_amount)) if min_amount and not pd.isna(min_amount) else None
        except Exception:
            clean_min = None
        try:
            clean_max = int(float(max_amount)) if max_amount and not pd.isna(max_amount) else None
        except Exception:
            clean_max = None
        return clean_min, clean_max, clean_currency, clean_period

    def parse_job_type(self, job_type_str):
        if not isinstance(job_type_str, str):
            return "Full-time"
        jt = job_type_str.lower()
        if "full" in jt:
            return "Full-time"
        elif "part" in jt:
            return "Part-time"
        elif "contract" in jt:
            return "Contract"
        elif "intern" in jt:
            return "Internship"
        return "Full-time"

    def determine_experience_level(self, title, description):
        # Robust handling if these aren't strings
        text = f"{self.safe_string(title)} {self.safe_string(description)}".lower()
        if any(word in text for word in ["senior", "sr.", "lead", "principal", "staff"]):
            return "Senior"
        elif any(word in text for word in ["junior", "jr.", "entry", "associate", "graduate", "new grad"]):
            return "Entry"
        elif any(word in text for word in ["manager", "director", "head", "vp", "vice president", "executive"]):
            return "Executive"
        return "Mid"

    def determine_location_type(self, location, description):
        text = f"{self.safe_string(location)} {self.safe_string(description)}".lower()
        if any(w in text for w in ["remote", "work from home", "wfh", "anywhere"]):
            if any(w in text for w in ["hybrid", "flexible", "occasional office"]):
                return "Hybrid"
            return "Remote"
        elif any(w in text for w in ["hybrid", "flexible"]):
            return "Hybrid"
        return "On-site"

    def get_or_create_company(self, db: Session, company_name: str, company_url: Optional[str] = None) -> Optional[Company]:
        if not company_name:
            return None
        # Defensive lookup to handle possible duplicates by name
        company = db.query(Company).filter(Company.name.ilike(f"%{company_name.strip()}%")).first()
        if company:
            return company
        try:
            company = Company(
                name=company_name.strip(),
                website_url=company_url,  # Correct field name
            )
            db.add(company)
            db.flush()  # Only flush, don't commit yet
            logger.info(f"Created new company: {company.name}")
            return company
        except Exception as e:
            logger.error(f"Error creating company {company_name}: {e}")
            return None

    def scrape_jobs(
        self,
        search_terms: List[str] = None,
        locations: List[str] = None,
        sites: List[str] = None,
        results_per_site: int = 50,
        hours_old: int = 24,
        job_type: str = None,
        is_remote: bool = False
    ) -> pd.DataFrame:
        from jobspy import scrape_jobs

        if search_terms is None:
            search_terms = ["Software Engineer AI", "Data Scientist", "Product Manager AI", "AI Engineer", "ML Engineer"]
        if locations is None:
            locations = ["India", "San Francisco, CA", "New York, NY", "Remote"]
        if sites is None:
            sites = ["linkedin", "indeed"]

        all_jobs = pd.DataFrame()
        for search_term in search_terms:
            for location in locations:
                try:
                    logger.info(f"Scraping jobs for '{search_term}' in '{location}'...")
                    scrape_params = dict(
                        site_name=sites,
                        search_term=search_term,
                        location=location,
                        results_wanted=results_per_site,
                        hours_old=hours_old,
                        linkedin_fetch_description=True,
                        description_format="markdown",
                        verbose=1,
                    )

                    # JobSpy defaults Indeed searches to the USA.
                    # Explicitly select India for India-based searches.
                    normalized_sites = [
                        str(site).lower() for site in
                        (sites if isinstance(sites, (list, tuple)) else [sites])
                    ]
                    if (
                        "india" in str(location).lower()
                        and "indeed" in normalized_sites
                    ):
                        scrape_params["country_indeed"] = "India"

                    if job_type:
                        scrape_params["job_type"] = job_type
                    if is_remote is True:
                        scrape_params["is_remote"] = True
                    jobs_df = scrape_jobs(**scrape_params)
                    if not jobs_df.empty:
                        jobs_df['search_term'] = search_term
                        jobs_df['search_location'] = location
                        all_jobs = pd.concat([all_jobs, jobs_df], ignore_index=True)
                        logger.info(f"Found {len(jobs_df)} jobs for '{search_term}' in '{location}'")
                    else:
                        logger.warning(f"No jobs found for '{search_term}' in '{location}'")
                except Exception as e:
                    logger.error(f"Error scraping jobs for '{search_term}' in '{location}': {e}")
                    continue
        logger.info(f"Total jobs scraped: {len(all_jobs)}")
        return all_jobs

    def store_jobs_in_db(self, db: Session, jobs_df: pd.DataFrame) -> int:
        if jobs_df.empty:
            return 0
        jobs_added = 0
        
         # Load existing identifiers to prevent database duplicates.
        existing_urls = {
            url for (url,) in
            db.query(Job.application_url)
            .filter(Job.application_url.isnot(None))
            .all()
        }

        existing_platform_ids = {
            str(platform_id) for (platform_id,) in
            db.query(Job.platform_job_id)
            .filter(Job.platform_job_id.isnot(None))
            .all()
        }

        # Track identifiers accepted during this scrape batch.
        seen_urls = set()
        seen_platform_ids = set()

        for _, job_row in jobs_df.iterrows():
            try:
                # Defensive: Get job_url
                job_url = self.safe_string(job_row.get('job_url')) or self.safe_string(job_row.get('job_url_direct'))
                if not job_url:
                    continue
                
                # Identify the source platform and extract its job ID.
                raw_platform = self.safe_string(
                    job_row.get('site')
                    or job_row.get('platform')
                    or job_url
                )

                platform_match = re.search(
                    r"(linkedin|indeed|glassdoor|google)",
                    raw_platform,
                    re.IGNORECASE
                )

                platform = (
                    platform_match.group(1).lower()
                    if platform_match else "UNKNOWN"
                )

                platform_job_id = None

                platform_id_patterns = {
                    "linkedin": r'/jobs/view/(\d+)',
                    "indeed": r'jk=(\w+)',
                    "glassdoor": r'Job-ID-(\d+)',
                    "google": r'jobs/view/(\d+)'
                }

                if platform in platform_id_patterns:
                    match = re.search(
                        platform_id_patterns[platform],
                        job_url
                    )

                    if match:
                        platform_job_id = match.group(1)

                # Skip URLs already in the database or this batch.
                if job_url in existing_urls or job_url in seen_urls:
                    continue

                # Skip platform IDs already in the database or this batch.
                if platform_job_id:
                    platform_id_key = str(platform_job_id)

                    if (
                        platform_id_key in existing_platform_ids
                        or platform_id_key in seen_platform_ids
                    ):
                        continue

                company_name = self.clean_str(job_row.get('company'))
                company_url = self.safe_string(job_row.get('company_url') or job_row.get('company_url_direct'))
                company = self.get_or_create_company(db, company_name, company_url)
                if not company:
                    logger.error(f"Skipping job with no valid company: {company_name}")
                    continue

                # Salary
                salary_min, salary_max, currency, period = self.clean_salary(
                    job_row.get('min_amount'),
                    job_row.get('max_amount'),
                    job_row.get('currency', 'USD'),
                    job_row.get('interval', 'year')
                )
                
                
                # Posted date
                posted_at = None
                date_posted = job_row.get('date_posted')
                if date_posted and not pd.isna(date_posted):
                    try:
                        posted_at = pd.to_datetime(date_posted)
                    except Exception:
                        posted_at = datetime.now() - timedelta(hours=24)
                # Title, description, location
                title = self.clean_str(job_row.get('title'))
                description = self.safe_string(job_row.get('description'))
                location = self.safe_string(job_row.get('location'))
                
                # Classify using the job title only.
                classification = classify_job(title)

                # Create one association for each confidently matched canonical role.
                role_associations = [
                    JobRoleAssociation(
                        canonical_role_id=role["canonical_role_id"],
                        professional_field_id=role["professional_field_id"],
                        subfield_id=role.get("subfield_id"),
                        additional_professional_field_ids=role.get("additional_professional_field_ids") or [],
                        match_type=role["match_type"],
                        matched_term=role.get("matched_term"),
                    )
                    for role in classification.get("roles", [])
                    if role.get("canonical_role_id")
                    and role.get("professional_field_id")
                ]

                job = Job(
                    company_id=company.id,
                    platform_job_id=platform_job_id,
                    title=title,
                    professional_field_id=classification.get("professional_field_id"),
                    subfield_id=classification.get("subfield_id"),
                    canonical_role_id=classification.get("canonical_role_id"),
                    role_associations=role_associations,
                    description=description,
                    location=location,
                    job_type=self.parse_job_type(job_row.get('job_type')),
                    experience_level=self.determine_experience_level(title, description),
                    location_type=self.determine_location_type(location, description),
                    salary_min=salary_min,
                    salary_max=salary_max,
                    salary_currency=currency,
                    salary_period=period,
                    application_url=job_url,
                    posted_at=posted_at,
                    is_active=True
                )
                db.add(job)
                # Mark identifiers as seen so duplicates in this batch are skipped.
                seen_urls.add(job_url)

                if platform_job_id:
                    seen_platform_ids.add(str(platform_job_id))
                jobs_added += 1
            except Exception as e:
                logger.error(f"Error storing job '{job_row.get('title', 'Unknown')}': {e}")
                continue
        try:
            db.commit()
            logger.info(f"Successfully stored {jobs_added} jobs in database")
        except Exception as e:
            logger.error(f"Error committing jobs to database: {e}")
            db.rollback()
            jobs_added = 0
        return jobs_added

    def scrape_and_store_jobs(
        self, 
        db: Session,
        search_terms: List[str] = None,
        locations: List[str] = None,
        max_jobs_per_query: int = 50
    ) -> int:
        try:
            jobs_df = self.scrape_jobs(
                search_terms=search_terms,
                locations=locations,
                results_per_site=max_jobs_per_query,
                hours_old=24,
                sites=["linkedin", "indeed"]
            )
            jobs_added = self.store_jobs_in_db(db, jobs_df)
            return jobs_added
        except Exception as e:
            logger.error(f"Error in scrape_and_store_jobs: {e}")
            return 0


job_service=JobSpyScraper()
# USAGE EXAMPLE

# if __name__ == "__main__":
#     scraper = JobSpyLinkedInScraper()
#     # Scrape jobs
#     jobs_df = scraper.scrape_jobs(
#         search_terms=["Software Engineer", "Python Developer"],
#         locations=["San Francisco, CA", "Remote"],
#         results_per_site=10
#     )
#     print(f"Scraped {len(jobs_df)} jobs")
#     if not jobs_df.empty:
#         print("Available columns:", jobs_df.columns.tolist())
#         display_cols = ['title', 'company', 'location', 'site']
#         available_cols = [col for col in display_cols if col in jobs_df.columns]
#         if available_cols:
#             print(jobs_df[available_cols].head())
#         else:
#             print(jobs_df.iloc[:, :4].head())
#     db = SessionLocal()
#     try:
#         jobs_added = scraper.store_jobs_in_db(db, jobs_df)
#         print(f"Added {jobs_added} jobs to database")
#     finally:
#         db.close()
