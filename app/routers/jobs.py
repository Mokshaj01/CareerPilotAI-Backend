from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, desc, asc, cast
from sqlalchemy.dialects.postgresql import JSONB
from typing import List, Optional
import math

from app.database import get_db
from app.models import User, Job, Company, UserScore, JobApplication, SavedJob, JobRoleAssociation
from app.schemas import (
    JobResponse, JobWithScore, JobSearchResponse, JobFilters,
    JobApplicationCreate, JobApplicationResponse, SavedJobCreate, SavedJobResponse
)
from app.services.auth import get_current_user

router = APIRouter()

@router.get("/search", response_model=JobSearchResponse)
async def search_jobs(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50),
    sort: Optional[str] = Query("recommended", regex="^(recommended|newest|match)$"),
    location: Optional[List[str]] = Query(None),
    job_type: Optional[List[str]] = Query(None),
    experience_level: Optional[List[str]] = Query(None),
    department: Optional[List[str]] = Query(None),
    company: Optional[List[str]] = Query(None),
    salary_min: Optional[int] = Query(None, ge=0),
    salary_max: Optional[int] = Query(None, ge=0),
    geographic_scope: Optional[str] = Query(None, pattern="^(India|Worldwide)$"),
    location_type: Optional[List[str]] = Query(None),
     # Professional taxonomy hierarchy filters
    professional_field_ids: Optional[List[str]] = Query(None),
    subfield_ids: Optional[List[str]] = Query(None),
    canonical_role_ids: Optional[List[str]] = Query(None),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Search jobs with filters, pagination, and sorting"""
    
    # Include every active job, even when no user-specific cluster score exists.
    # The score is optional; personalized recommendations use a separate endpoint.
    query = db.query(Job, UserScore).outerjoin(
        UserScore, and_(
            Job.cluster_id == UserScore.cluster_id,
            UserScore.user_id == current_user.id
        )
    ).join(Company).filter(
        Job.is_active == True
    )
    
    # Apply filters
    if location:
        location_conditions = []
        for loc in location:
            location_conditions.append(Job.location.ilike(f"%{loc}%"))
        query = query.filter(or_(*location_conditions))
    
    if geographic_scope == "India":
        query = query.filter(
            or_(
                Job.location.ilike("%India"),
                Job.location.ilike("%, IN"),
                Job.location.ilike("%, IN,%"),
            )
        )

    if location_type:
        query = query.filter(Job.location_type.in_(location_type))
        
    # Professional taxonomy hierarchy filters
    # Multiple selections within each level use OR.
    # Different hierarchy levels are combined using AND.

    if professional_field_ids:
        field_association_conditions = [
            JobRoleAssociation.professional_field_id.in_(professional_field_ids)
        ]

        field_association_conditions.extend(
            cast(
                JobRoleAssociation.additional_professional_field_ids,
                JSONB
            ).contains([field_id])
            for field_id in professional_field_ids
        )

        query = query.filter(
            or_(
                Job.professional_field_id.in_(professional_field_ids),
                Job.role_associations.any(
                    or_(*field_association_conditions)
                )
            )
        )

    if subfield_ids:
        query = query.filter(
            Job.subfield_id.in_(subfield_ids)
        )

    if canonical_role_ids:
        query = query.filter(
            Job.canonical_role_id.in_(canonical_role_ids)
        )    

    if job_type:
        query = query.filter(Job.job_type.in_(job_type))
    
    if experience_level:
        query = query.filter(Job.experience_level.in_(experience_level))
    
    if department:
        query = query.filter(Job.department.in_(department))
    
    if company:
        query = query.filter(Company.name.in_(company))
    
    if salary_min:
        query = query.filter(
            or_(Job.salary_min >= salary_min, Job.salary_min.is_(None))
        )
    
    if salary_max:
        query = query.filter(
            or_(Job.salary_max <= salary_max, Job.salary_max.is_(None))
        )
    
    # Apply sorting
    if sort == "newest":
        query = query.order_by(desc(Job.posted_at), desc(Job.scraped_at))
    elif sort == "match":
        query = query.order_by(desc(UserScore.final_score))
    else:  # recommended (default)
        # Recommended uses a combination of score and recency
        query = query.order_by(desc(UserScore.final_score), desc(Job.posted_at))
    
    # Get total count before pagination
    total = query.count()
    total_pages = math.ceil(total / limit) if total > 0 else 1
    
    # Apply pagination
    offset = (page - 1) * limit
    results = query.offset(offset).limit(limit).all()
    
    # Format results
    jobs_with_scores = []
    for job, score in results:
        job_dict = _format_job_with_score(job, score)
        jobs_with_scores.append(job_dict)
    
    # Get filter options
    filters = _get_filter_options(db)
    
    return {
        "jobs": jobs_with_scores,
        "total": total,
        "page": page,
        "total_pages": total_pages,
        "filters": filters
    }

@router.get("/recommended", response_model=List[JobWithScore])
async def get_recommended_jobs(
    limit: int = Query(20, ge=1, le=50),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get top recommended jobs for the user"""
    
    # Get jobs ordered by user's scores with recency boost
    results = db.query(Job, UserScore).join(
        UserScore, and_(
            Job.cluster_id == UserScore.cluster_id,
            UserScore.user_id == current_user.id
        )
    ).join(Company).filter(
        Job.is_active == True,
        UserScore.cluster_id.isnot(None)
    ).order_by(
        desc(UserScore.final_score),
        desc(Job.posted_at)
    ).limit(limit).all()
    
    jobs_with_scores = []
    for job, score in results:
        job_dict = _format_job_with_score(job, score)
        jobs_with_scores.append(job_dict)
    
    return jobs_with_scores

@router.get("/{job_id}", response_model=JobWithScore)
async def get_job_details(
    job_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get detailed job information with user score"""
    
    result = db.query(Job, UserScore).join(
        UserScore, and_(
            Job.cluster_id == UserScore.cluster_id,
            UserScore.user_id == current_user.id
        )
    ).join(Company).filter(
        Job.id == job_id,
        Job.is_active == True
    ).first()
    
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )
    
    job, score = result
    return _format_job_with_score(job, score)

@router.post("/apply", response_model=JobApplicationResponse)
async def apply_to_job(
    application: JobApplicationCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Apply to a job"""
    
    # Check if job exists
    job = db.query(Job).filter(Job.id == application.job_id, Job.is_active == True).first()
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )
    
    # Check if already applied
    existing_application = db.query(JobApplication).filter(
        JobApplication.user_id == current_user.id,
        JobApplication.job_id == application.job_id
    ).first()
    
    if existing_application:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Already applied to this job"
        )
    
    # Create application
    job_application = JobApplication(
        user_id=current_user.id,
        job_id=application.job_id
    )
    
    db.add(job_application)
    db.commit()
    db.refresh(job_application)
    
    return {
        "id": job_application.id,
        "user_id": job_application.user_id,
        "job_id": job_application.job_id,
        "status": job_application.status,
        "applied_at": job_application.applied_at
    }

@router.get("/applications/my", response_model=List[JobApplicationResponse])
async def get_my_applications(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get user's job applications"""
    
    applications = db.query(JobApplication).filter(
        JobApplication.user_id == current_user.id
    ).order_by(desc(JobApplication.applied_at)).all()
    
    return [
        {
            "id": app.id,
            "user_id": app.user_id,
            "job_id": app.job_id,
            "status": app.status,
            "applied_at": app.applied_at
        }
        for app in applications
    ]

@router.get("/applications/my/detailed", response_model=JobSearchResponse)
async def get_my_applications_detailed(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get user's job applications with full job details and pagination"""
    
    # Build base query for applications with job details and scores
    base_query = db.query(Job, UserScore, JobApplication).join(
        JobApplication, Job.id == JobApplication.job_id
    ).join(
        UserScore, and_(
            Job.cluster_id == UserScore.cluster_id,
            UserScore.user_id == current_user.id
        )
    ).join(Company).filter(
        JobApplication.user_id == current_user.id,
        Job.is_active == True
    )
    
    # Get total count
    total = base_query.count()
    total_pages = math.ceil(total / limit) if total > 0 else 1
    
    # Apply pagination and ordering
    offset = (page - 1) * limit
    results = base_query.order_by(desc(JobApplication.applied_at)).offset(offset).limit(limit).all()
    
    jobs_with_scores = []
    for job, score, application in results:
        job_dict = _format_job_with_score(job, score)
        # Add application details
        job_dict["application"] = {
            "id": application.id,
            "status": application.status,
            "applied_at": application.applied_at
        }
        jobs_with_scores.append(job_dict)
    
    return {
        "jobs": jobs_with_scores,
        "total": total,
        "page": page,
        "total_pages": total_pages,
        "filters": {
            "locations": [],
            "job_types": [],
            "experience_levels": [],
            "departments": [],
            "companies": []
        }
    }

@router.post("/save", response_model=SavedJobResponse)
async def save_job(
    saved_job: SavedJobCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Save a job for later"""
    
    # Check if job exists
    job = db.query(Job).filter(Job.id == saved_job.job_id, Job.is_active == True).first()
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )
    
    # Check if already saved
    existing_saved = db.query(SavedJob).filter(
        SavedJob.user_id == current_user.id,
        SavedJob.job_id == saved_job.job_id
    ).first()
    
    if existing_saved:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Job already saved"
        )
    
    # Save job
    saved_job_record = SavedJob(
        user_id=current_user.id,
        job_id=saved_job.job_id
    )
    
    db.add(saved_job_record)
    db.commit()
    db.refresh(saved_job_record)
    
    return {
        "id": saved_job_record.id,
        "user_id": saved_job_record.user_id,
        "job_id": saved_job_record.job_id,
        "saved_at": saved_job_record.saved_at,
        "job": _format_job_basic(job)
    }

@router.get("/saved/my", response_model=List[SavedJobResponse])
async def get_my_saved_jobs(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get user's saved jobs"""
    
    # Fix: Properly join with Job and Company to get job details
    saved_jobs = db.query(SavedJob, Job, Company).join(
        Job, SavedJob.job_id == Job.id
    ).join(
        Company, Job.company_id == Company.id
    ).filter(
        SavedJob.user_id == current_user.id,
        Job.is_active == True
    ).order_by(desc(SavedJob.saved_at)).all()
    
    return [
        {
            "id": saved.id,
            "user_id": saved.user_id,
            "job_id": saved.job_id,
            "saved_at": saved.saved_at,
            "job": {
                "id": job.id,
                "title": job.title,
                "company": {
                    "id": company.id,
                    "name": company.name
                },
                "location": job.location,
                "job_type": job.job_type,
                "posted_at": job.posted_at,
                "created_at": job.created_at
            }
        }
        for saved, job, company in saved_jobs
    ]
    
@router.get("/saved/my/detailed", response_model=JobSearchResponse)
async def get_my_saved_jobs_detailed(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get user's saved jobs with full job details, scores, and pagination"""
    
    # Build base query for saved jobs with job details and scores
    base_query = db.query(Job, UserScore, SavedJob).join(
        SavedJob, Job.id == SavedJob.job_id
    ).join(
        UserScore, and_(
            Job.cluster_id == UserScore.cluster_id,
            UserScore.user_id == current_user.id
        )
    ).join(Company).filter(
        SavedJob.user_id == current_user.id,
        Job.is_active == True
    )
    
    # Get total count
    total = base_query.count()
    total_pages = math.ceil(total / limit) if total > 0 else 1
    
    # Apply pagination and ordering
    offset = (page - 1) * limit
    results = base_query.order_by(desc(SavedJob.saved_at)).offset(offset).limit(limit).all()
    
    jobs_with_scores = []
    for job, score, saved in results:
        job_dict = _format_job_with_score(job, score)
        # Add saved details
        job_dict["saved"] = {
            "id": saved.id,
            "saved_at": saved.saved_at
        }
        jobs_with_scores.append(job_dict)
    
    return {
        "jobs": jobs_with_scores,
        "total": total,
        "page": page,
        "total_pages": total_pages,
        "filters": {
            "locations": [],
            "job_types": [],
            "experience_levels": [],
            "departments": [],
            "companies": []
        }
    }

@router.delete("/saved/{job_id}")
async def unsave_job(
    job_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Remove a job from saved jobs"""
    
    saved_job = db.query(SavedJob).filter(
        SavedJob.user_id == current_user.id,
        SavedJob.job_id == job_id
    ).first()
    
    if not saved_job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Saved job not found"
        )
    
    db.delete(saved_job)
    db.commit()
    
    return {"message": "Job removed from saved jobs"}

def _format_job_with_score(job: Job, score: Optional[UserScore]) -> dict:
    """Format job with score data"""
    return {
        "id": job.id,
        "company_id": job.company_id,
        "platform_job_id": job.platform_job_id,
        "platform": job.platform,
        "title": job.title,
        "description": job.description,
        "requirements": job.requirements,
        "benefits": job.benefits,
        "location": job.location,
        "location_type": job.location_type,
        "job_type": job.job_type,
        "experience_level": job.experience_level,
        "department": job.department,
        "salary_min": job.salary_min,
        "salary_max": job.salary_max,
        "salary_currency": job.salary_currency,
        "salary_period": job.salary_period,
        "application_url": job.application_url,
        "applicants_count": job.applicants_count,
        "cluster_id": job.cluster_id,
        "is_active": job.is_active,
        "professional_field_id": job.professional_field_id,
        "subfield_id": job.subfield_id,
        "canonical_role_id": job.canonical_role_id,
        "listing_status": job.listing_status,
        "application_deadline": job.application_deadline,
        "status_verified_at": job.status_verified_at,
        "posted_at": job.posted_at,
        "scraped_at": job.scraped_at,
        "created_at": job.created_at,
        "company": {
            "id": job.company.id,
            "name": job.company.name,
            "description": job.company.description,
            "industry": job.company.industry,
            "company_size": job.company.company_size,
            "headquarters": job.company.headquarters,
            "website_url": job.company.website_url,
            "logo_url": job.company.logo_url,
            "stage": job.company.stage,
            "created_at": job.company.created_at
        },
        "match_score": score.final_score if score else None,
        "match_type": score.match_type if score else None,
        "experience_score": score.experience_score if score else None,
        "skills_score": score.skills_score if score else None,
        "education_score": score.education_score if score else None,
        "projects_score": score.projects_score if score else None,
        "certifications_score": score.certifications_score if score else None
    }

def _format_job_basic(job: Job) -> dict:
    """Format basic job data without scores"""
    return {
        "id": job.id,
        "title": job.title,
        "company": {
            "id": job.company.id if job.company else None,
            "name": job.company.name if job.company else None
        },
        "location": job.location,
        "job_type": job.job_type,
        "posted_at": job.posted_at,
        "created_at": job.created_at
    }

def _get_filter_options(db: Session) -> dict:
    """Get available filter options"""
    
    # Get distinct values for filters
    locations = db.query(Job.location).filter(
        Job.is_active == True,
        Job.location.isnot(None)
    ).distinct().all()
    
    job_types = db.query(Job.job_type).filter(
        Job.is_active == True,
        Job.job_type.isnot(None)
    ).distinct().all()
    
    experience_levels = db.query(Job.experience_level).filter(
        Job.is_active == True,
        Job.experience_level.isnot(None)
    ).distinct().all()
    
    departments = db.query(Job.department).filter(
        Job.is_active == True,
        Job.department.isnot(None)
    ).distinct().all()
    
    companies = db.query(Company.name).join(Job).filter(
        Job.is_active == True
    ).distinct().all()
    
    return {
        "locations": [loc[0] for loc in locations if loc[0]],
        "job_types": [jt[0] for jt in job_types if jt[0]],
        "experience_levels": [el[0] for el in experience_levels if el[0]],
        "departments": [dept[0] for dept in departments if dept[0]],
        "companies": [comp[0] for comp in companies if comp[0]]
    }
