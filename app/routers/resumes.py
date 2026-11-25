from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List
import os
import uuid
from pathlib import Path

from app.database import get_db
from app.models import User, Resume, UserProfile, UserScore
from app.schemas import ResumeResponse, ResumeUpload, ParsedResumeData, UserProfileCreate
from app.services.auth import get_current_user
from app.services.resume_parser import resume_parser
from app.services.embedding_service import embedding_service
from app.services.scoring_service import scoring_service
from app.core.config import settings

router = APIRouter()

# Ensure upload directory exists
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

@router.post("/upload", response_model=ResumeResponse)
async def upload_resume(
    file: UploadFile = File(...),
    target_job_title: str = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Upload and parse a resume"""
    
    # Validate file type
    allowed_types = ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF and DOCX files are allowed"
        )
    
    # Validate file size
    contents = await file.read()
    if len(contents) > settings.MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File size exceeds maximum allowed size of {settings.MAX_FILE_SIZE} bytes"
        )
    
    try:
        # Generate unique filename
        file_extension = Path(file.filename).suffix.lower()
        unique_filename = f"{uuid.uuid4()}{file_extension}"
        file_path = os.path.join(settings.UPLOAD_DIR, unique_filename)
        
        # Save file
        with open(file_path, "wb") as f:
            f.write(contents)
        
        # Extract text from file
        file_type = "pdf" if file_extension == ".pdf" else "docx"
        raw_text = resume_parser.extract_text_from_file(contents, file_type)
        
        # Parse resume with Gemini
        parsed_data = resume_parser.parse_resume_with_gemini(raw_text)
        
        # Check if there's already a primary resume
        existing_primary = db.query(Resume).filter(
            Resume.user_id == current_user.id,
            Resume.is_primary == True
        ).first()
        
        # If no primary resume exists, make this one primary
        is_primary = existing_primary is None
        
        # Initialize embedding variables
        resume_embeddings = {}
        
        # Only generate embeddings and calculate scores for primary resume
        if is_primary:
            # Generate embeddings for different sections
            resume_embeddings = embedding_service.generate_resume_embeddings(parsed_data)
        
        # Create resume record
        resume = Resume(
            user_id=current_user.id,
            filename=unique_filename,
            original_filename=file.filename,
            file_path=file_path,
            file_size=len(contents),
            file_type=file_extension,
            raw_text=raw_text,
            parsed_data=parsed_data,
            experience_embedding=resume_embeddings.get('experience') if is_primary else None,
            skills_embedding=resume_embeddings.get('skills') if is_primary else None,
            education_embedding=resume_embeddings.get('education') if is_primary else None,
            projects_embedding=resume_embeddings.get('projects') if is_primary else None,
            certifications_embedding=resume_embeddings.get('certifications') if is_primary else None,
            is_primary=is_primary,
            target_job_title=target_job_title
        )
        
        db.add(resume)
        db.commit()
        db.refresh(resume)
        
        # Only update profile and calculate scores for primary resume
        if is_primary:
            # Update user profile with parsed data
            await _update_user_profile_from_resume(db, current_user.id, parsed_data)
            
            # Calculate job scores for this user
            scoring_service.calculate_user_job_scores(db, current_user.id, resume.id)
        
        return resume
        
    except Exception as e:
        # Clean up file if something went wrong
        if 'file_path' in locals() and os.path.exists(file_path):
            os.remove(file_path)
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing resume: {str(e)}"
        )

@router.get("/", response_model=List[ResumeResponse])
async def get_user_resumes(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all resumes for the current user"""
    resumes = db.query(Resume).filter(Resume.user_id == current_user.id).all()
    return resumes

@router.get("/slots")
async def get_resume_slots(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get resume slot usage for the current user."""
    used = db.query(Resume).filter(
        Resume.user_id == current_user.id
    ).count()

    return {
        "used": used,
        "total": 5
    }

@router.get("/{resume_id}", response_model=ResumeResponse)
async def get_resume(
    resume_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get a specific resume"""
    resume = db.query(Resume).filter(
        Resume.id == resume_id,
        Resume.user_id == current_user.id
    ).first()
    
    if not resume:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume not found"
        )
    
    return resume

@router.get("/{resume_id}/parsed-data", response_model=ParsedResumeData)
async def get_parsed_resume_data(
    resume_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get parsed data for a specific resume"""
    resume = db.query(Resume).filter(
        Resume.id == resume_id,
        Resume.user_id == current_user.id
    ).first()
    
    if not resume:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume not found"
        )
    
    return resume.parsed_data

@router.get("/{resume_id}/download")
async def download_resume(
    resume_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Download a resume file"""
    resume = db.query(Resume).filter(
        Resume.id == resume_id,
        Resume.user_id == current_user.id
    ).first()
    
    if not resume:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume not found"
        )
    
    if not os.path.exists(resume.file_path):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume file not found on server"
        )
    
    return FileResponse(
        path=resume.file_path,
        filename=resume.original_filename,
        media_type="application/octet-stream"
    )

@router.put("/{resume_id}/set-primary")
async def set_primary_resume(
    resume_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Set a resume as primary"""
    resume = db.query(Resume).filter(
        Resume.id == resume_id,
        Resume.user_id == current_user.id
    ).first()
    
    if not resume:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume not found"
        )
    
    # If it's already primary, no need to do anything
    if resume.is_primary:
        return {"message": "Resume is already primary"}
    
    # Get the current primary resume (if any)
    current_primary = db.query(Resume).filter(
        Resume.user_id == current_user.id,
        Resume.is_primary == True
    ).first()
    
    # Unset current primary
    if current_primary:
        current_primary.is_primary = False
        
        # Clear embeddings from old primary resume (optional - to save space)
        current_primary.experience_embedding = None
        current_primary.skills_embedding = None
        current_primary.education_embedding = None
        current_primary.projects_embedding = None
        current_primary.certifications_embedding = None
    
    # Set this resume as primary
    resume.is_primary = True
    
    # Generate embeddings for the new primary resume if not already present
    if not resume.experience_embedding:
        resume_embeddings = embedding_service.generate_resume_embeddings(resume.parsed_data)
        resume.experience_embedding = resume_embeddings.get('experience')
        resume.skills_embedding = resume_embeddings.get('skills')
        resume.education_embedding = resume_embeddings.get('education')
        resume.projects_embedding = resume_embeddings.get('projects')
        resume.certifications_embedding = resume_embeddings.get('certifications')
    
    db.commit()
    
    # Update user profile with new primary resume data
    await _update_user_profile_from_resume(db, current_user.id, resume.parsed_data)
    
    # Recalculate job scores with new primary resume
    scoring_service.calculate_user_job_scores(db, current_user.id, resume.id)
    
    return {"message": "Resume set as primary successfully"}

@router.delete("/{resume_id}")
async def delete_resume(
    resume_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete a resume"""
    resume = db.query(Resume).filter(
        Resume.id == resume_id,
        Resume.user_id == current_user.id
    ).first()
    
    if not resume:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume not found"
        )
    
    # Delete file from filesystem
    if os.path.exists(resume.file_path):
        os.remove(resume.file_path)
    
    # Check if this was the primary resume
    was_primary = resume.is_primary
    
    # Delete the resume
    db.delete(resume)
    db.commit()
    
    # If deleted resume was primary, set another resume as primary and recalculate
    if was_primary:
        # Set the most recent resume as primary
        new_primary = db.query(Resume).filter(
            Resume.user_id == current_user.id
        ).order_by(Resume.created_at.desc()).first()
        
        if new_primary:
            new_primary.is_primary = True
            
            # Generate embeddings for new primary resume if not present
            if not new_primary.experience_embedding:
                resume_embeddings = embedding_service.generate_resume_embeddings(new_primary.parsed_data)
                new_primary.experience_embedding = resume_embeddings.get('experience')
                new_primary.skills_embedding = resume_embeddings.get('skills')
                new_primary.education_embedding = resume_embeddings.get('education')
                new_primary.projects_embedding = resume_embeddings.get('projects')
                new_primary.certifications_embedding = resume_embeddings.get('certifications')
            
            db.commit()
            
            # Update user profile with new primary resume data
            await _update_user_profile_from_resume(db, current_user.id, new_primary.parsed_data)
            
            # Recalculate scores with new primary resume
            scoring_service.calculate_user_job_scores(db, current_user.id, new_primary.id)
        else:
            # No resumes left, clear user profile resume-related data
            profile = db.query(UserProfile).filter(UserProfile.user_id == current_user.id).first()
            if profile:
                profile.experience = None
                profile.skills = None
                profile.education = None
                profile.projects = None
                profile.certifications = None
                profile.languages = None
                db.commit()
            
            # Clear user scores since no primary resume exists
            db.query(UserScore).filter(UserScore.user_id == current_user.id).delete()
            db.commit()
    
    return {"message": "Resume deleted successfully"}

@router.post("/{resume_id}/reparse")
async def reparse_resume(
    resume_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Reparse a resume with updated parsing logic"""
    resume = db.query(Resume).filter(
        Resume.id == resume_id,
        Resume.user_id == current_user.id
    ).first()
    
    if not resume:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume not found"
        )
    
    try:
        # Re-parse the existing raw text
        parsed_data = resume_parser.parse_resume_with_gemini(resume.raw_text)
        
        # Generate new embeddings
        resume_embeddings = embedding_service.generate_resume_embeddings(parsed_data)
        
        # Update resume record
        resume.parsed_data = parsed_data
        resume.experience_embedding = resume_embeddings.get('experience')
        resume.skills_embedding = resume_embeddings.get('skills')
        resume.education_embedding = resume_embeddings.get('education')
        resume.projects_embedding = resume_embeddings.get('projects')
        resume.certifications_embedding = resume_embeddings.get('certifications')
        
        db.commit()
        
        # Update user profile
        await _update_user_profile_from_resume(db, current_user.id, parsed_data)
        
        # Recalculate job scores
        scoring_service.calculate_user_job_scores(db, current_user.id, resume.id)
        
        return {"message": "Resume reparsed successfully"}
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error reparsing resume: {str(e)}"
        )

async def _update_user_profile_from_resume(db: Session, user_id: int, parsed_data: dict):
    """Update user profile with data from parsed resume"""
    
    # Get or create user profile
    profile = db.query(UserProfile).filter(UserProfile.user_id == user_id).first()
    
    if not profile:
        profile = UserProfile(user_id=user_id)
        db.add(profile)
    
    # Update profile data from parsed resume
    personal_info = parsed_data.get("personal_info", {})
    
    if personal_info.get("phone") and not profile.phone:
        profile.phone = personal_info["phone"]

    if personal_info.get("name") and not profile.name:
        profile.name = personal_info["name"]

    if personal_info.get("email") and not profile.email:
        profile.email = personal_info["email"]
            
    if personal_info.get("location") and not profile.location:
        profile.location = personal_info["location"]
    
    if personal_info.get("linkedin") and not profile.linkedin_url:
        profile.linkedin_url = personal_info["linkedin"]
    
    if personal_info.get("github") and not profile.github_url:
        profile.github_url = personal_info["github"]
    
    if personal_info.get("portfolio") and not profile.portfolio_url:
        profile.portfolio_url = personal_info["portfolio"]
    
    if personal_info.get("summary") and not profile.summary:
        profile.summary = personal_info["summary"]
    
    # Update structured data
    if parsed_data.get("experience"):
        profile.experience = parsed_data["experience"]
    
    if parsed_data.get("skills"):
        # Extract all skills into a flat list
        all_skills = []
        skills_data = parsed_data["skills"]
        if isinstance(skills_data, dict):
            for skill_category in skills_data.values():
                if isinstance(skill_category, list):
                    all_skills.extend(skill_category)
        elif isinstance(skills_data, list):
            all_skills = skills_data
        
        profile.skills = list(set(all_skills))  # Remove duplicates
    
    if parsed_data.get("education"):
        profile.education = parsed_data["education"]
    
    if parsed_data.get("projects"):
        profile.projects = parsed_data["projects"]
    
    if parsed_data.get("certifications"):
        profile.certifications = parsed_data["certifications"]
    
    if parsed_data.get("languages"):
        profile.languages = parsed_data["languages"]
    
    db.commit()