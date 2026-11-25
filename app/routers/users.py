from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import Resume, User, UserProfile, UserScore
from app.schemas import (
    UserResponse, UserProfileCreate, UserProfileResponse, UserScoreResponse
)

from app.services.auth import get_current_user
from app.services.scoring_service import scoring_service

router = APIRouter()

@router.get("/profile", response_model=UserProfileResponse)
async def get_user_profile(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get current user's profile with primary resume details"""
    profile = db.query(UserProfile).filter(UserProfile.user_id == current_user.id).first()
    
    if not profile:
        # Create empty profile if doesn't exist
        profile = UserProfile(user_id=current_user.id)
        db.add(profile)
        db.commit()
        db.refresh(profile)
    
    # Get primary resume details
    primary_resume = db.query(Resume).filter(
        Resume.user_id == current_user.id,
        Resume.is_primary == True
    ).first()
    
    # Create response with profile and primary resume info
    profile_response = {
        **profile.__dict__,
        "primary_resume": None
    }
    
    if primary_resume:
        profile_response["primary_resume"] = {
            "id": primary_resume.id,
            "original_filename": primary_resume.original_filename,
            "target_job_title": primary_resume.target_job_title,
            "created_at": primary_resume.created_at,
            "updated_at": primary_resume.updated_at,
            "parsed_data": primary_resume.parsed_data
        }
        
        # If profile data is empty but primary resume has data, populate from resume
        if primary_resume.parsed_data:
            personal_info = primary_resume.parsed_data.get("personal_info", {})
            
            # Only update if profile fields are empty
            if not profile.name and personal_info.get("name"):
                profile_response["name"] = personal_info["name"]
            if not profile.email and personal_info.get("email"):
                profile_response["email"] = personal_info["email"]
            if not profile.phone and personal_info.get("phone"):
                profile_response["phone"] = personal_info["phone"]
            if not profile.location and personal_info.get("location"):
                profile_response["location"] = personal_info["location"]
            if not profile.linkedin_url and personal_info.get("linkedin"):
                profile_response["linkedin_url"] = personal_info["linkedin"]
            if not profile.github_url and personal_info.get("github"):
                profile_response["github_url"] = personal_info["github"]
            if not profile.portfolio_url and personal_info.get("portfolio"):
                profile_response["portfolio_url"] = personal_info["portfolio"]
            if not profile.summary and personal_info.get("summary"):
                profile_response["summary"] = personal_info["summary"]
            
            # Update structured data from primary resume if not present in profile
            if not profile.experience and primary_resume.parsed_data.get("experience"):
                profile_response["experience"] = primary_resume.parsed_data["experience"]
            if not profile.skills and primary_resume.parsed_data.get("skills"):
                skills_data = primary_resume.parsed_data["skills"]
                all_skills = []
                if isinstance(skills_data, dict):
                    for skill_category in skills_data.values():
                        if isinstance(skill_category, list):
                            all_skills.extend(skill_category)
                elif isinstance(skills_data, list):
                    all_skills = skills_data
                profile_response["skills"] = list(set(all_skills))
            if not profile.education and primary_resume.parsed_data.get("education"):
                profile_response["education"] = primary_resume.parsed_data["education"]
            if not profile.projects and primary_resume.parsed_data.get("projects"):
                profile_response["projects"] = primary_resume.parsed_data["projects"]
            if not profile.certifications and primary_resume.parsed_data.get("certifications"):
                profile_response["certifications"] = primary_resume.parsed_data["certifications"]
            if not profile.languages and primary_resume.parsed_data.get("languages"):
                profile_response["languages"] = primary_resume.parsed_data["languages"]
    
    return profile_response


@router.get("/profile/resume-stats")
async def get_profile_resume_stats(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get resume statistics for the profile"""
    from app.models import Resume
    
    # Count total resumes
    total_resumes = db.query(Resume).filter(Resume.user_id == current_user.id).count()
    
    # Get primary resume
    primary_resume = db.query(Resume).filter(
        Resume.user_id == current_user.id,
        Resume.is_primary == True
    ).first()
    
    # Get all resumes with basic info
    all_resumes = db.query(Resume).filter(Resume.user_id == current_user.id).all()
    
    resume_list = []
    for resume in all_resumes:
        resume_list.append({
            "id": resume.id,
            "original_filename": resume.original_filename,
            "is_primary": resume.is_primary,
            "target_job_title": resume.target_job_title,
            "created_at": resume.created_at,
            "has_embeddings": bool(resume.experience_embedding)
        })
    
    return {
        "total_resumes": total_resumes,
        "primary_resume_id": primary_resume.id if primary_resume else None,
        "resumes": resume_list
    }
    
@router.put("/profile", response_model=UserProfileResponse)
async def update_user_profile(
    profile_data: UserProfileCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update current user's profile"""
    profile = db.query(UserProfile).filter(UserProfile.user_id == current_user.id).first()
    
    if not profile:
        profile = UserProfile(user_id=current_user.id)
        db.add(profile)
    
    # Update profile fields
    for field, value in profile_data.dict(exclude_unset=True).items():
        setattr(profile, field, value)
    
    db.commit()
    db.refresh(profile)
    
    # Recalculate job scores if relevant fields changed
    if any(field in profile_data.dict(exclude_unset=True) for field in 
           ['skills', 'experience', 'education', 'projects', 'certifications']):
        scoring_service.calculate_user_job_scores(db, current_user.id)
    
    return profile

@router.get("/scores", response_model=List[UserScoreResponse])
async def get_user_scores(
    limit: int = 20,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get user's job scores"""
    scores = db.query(UserScore).filter(
        UserScore.user_id == current_user.id,
        UserScore.cluster_id.isnot(None)
    ).order_by(UserScore.final_score.desc()).limit(limit).all()
    
    return scores

@router.post("/recalculate-scores")
async def recalculate_user_scores(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Manually trigger recalculation of user's job scores"""
    scoring_service.calculate_user_job_scores(db, current_user.id)
    return {"message": "Job scores recalculated successfully"}

@router.get("/dashboard-stats")
async def get_dashboard_stats(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get dashboard statistics for the user"""
    from app.models import Resume, JobApplication, SavedJob, Job
    
    # Count resumes
    resume_count = db.query(Resume).filter(Resume.user_id == current_user.id).count()
    
    # Count applications
    application_count = db.query(JobApplication).filter(
        JobApplication.user_id == current_user.id
    ).count()
    
    # Count saved jobs
    saved_jobs_count = db.query(SavedJob).filter(
        SavedJob.user_id == current_user.id
    ).count()
    
    # Get top match score
    top_score = db.query(UserScore).filter(
        UserScore.user_id == current_user.id,
        UserScore.cluster_id.isnot(None)
    ).order_by(UserScore.final_score.desc()).first()
    
    # Count total available jobs
    total_jobs = db.query(Job).filter(Job.is_active == True).count()
    
    return {
        "resume_count": resume_count,
        "application_count": application_count,
        "saved_jobs_count": saved_jobs_count,
        "top_match_score": top_score.final_score if top_score else 0,
        "total_jobs_available": total_jobs
    }

@router.delete("/account")
async def delete_user_account(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete user account and all associated data"""
    from app.models import Resume, JobApplication, SavedJob
    import os
    
    # Delete user's resume files
    resumes = db.query(Resume).filter(Resume.user_id == current_user.id).all()
    for resume in resumes:
        if os.path.exists(resume.file_path):
            os.remove(resume.file_path)
    
    # Delete all user data (cascading deletes will handle related records)
    db.delete(current_user)
    db.commit()
    
    return {"message": "Account deleted successfully"}