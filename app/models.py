from typing import Optional
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, Float, ForeignKey, JSON, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    profile = relationship("UserProfile", back_populates="user", uselist=False)
    resumes = relationship("Resume", back_populates="user")
    scores = relationship("UserScore", back_populates="user")

    # Add these missing relationships
    applications = relationship("JobApplication", back_populates="user")
    saved_jobs = relationship("SavedJob", back_populates="user")
    
    profile_picture: Optional[str] = Column(String, nullable=True)
    is_oauth_user: Optional[bool] = Column(Boolean, default=False)

class UserProfile(Base):
    __tablename__ = "user_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    
    # Personal Information
    phone = Column(String)
    name= Column(String)
    email = Column(String)
    location = Column(String)
    linkedin_url = Column(String)
    github_url = Column(String)
    portfolio_url = Column(String)
    
    # Professional Summary
    summary = Column(Text)
    
    # Experience (JSON array of objects)
    experience = Column(JSON)  # [{"company": "", "position": "", "duration": "", "description": ""}]
    
    # Skills (JSON array)
    skills = Column(JSON)  # ["Python", "Machine Learning", ...]
    
    # Education (JSON array of objects)
    education = Column(JSON)  # [{"institution": "", "degree": "", "year": "", "gpa": ""}]
    
    # Projects (JSON array of objects)
    projects = Column(JSON)  # [{"name": "", "description": "", "technologies": [], "url": ""}]
    
    # Certifications (JSON array of objects)
    certifications = Column(JSON)  # [{"name": "", "issuer": "", "date": "", "url": ""}]
    
    # Languages (JSON array of objects)
    languages = Column(JSON)  # [{"language": "", "proficiency": ""}]
    
    # Job Preferences
    preferred_job_types = Column(JSON)  # ["Full-time", "Remote"]
    preferred_locations = Column(JSON)  # ["San Francisco", "Remote"]
    salary_expectation_min = Column(Integer)
    salary_expectation_max = Column(Integer)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="profile")

class Company(Base):
    __tablename__ = "companies"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    linkedin_id = Column(String, unique=True, index=True)
    
    # Company Details
    description = Column(Text)
    industry = Column(String)
    company_size = Column(String)  # "1-10", "11-50", etc.
    headquarters = Column(String)
    website_url = Column(String)
    logo_url = Column(String)
    
    # Company Stage
    stage = Column(String)  # "Early Stage", "Late Stage", "Public Company"
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    jobs = relationship("Job", back_populates="company")

class Job(Base):
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    platform_job_id = Column(String, unique=True, index=True)
    platform = Column(String, default="UNKNOWN")
    
    # Job Details
    title = Column(String, nullable=False)
    description = Column(Text)
    requirements = Column(Text)
    benefits = Column(Text)
    
    # Job Meta
    location = Column(String)
    location_type = Column(String)  # "Remote", "On-site", "Hybrid"
    job_type = Column(String)  # "Full-time", "Part-time", "Contract", "Internship"
    experience_level = Column(String)  # "Entry", "Mid", "Senior", "Executive"
    department = Column(String)
    
    # Salary Information
    salary_min = Column(Integer)
    salary_max = Column(Integer)
    salary_currency = Column(String, default="USD")
    salary_period = Column(String, default="year")  # "hour", "month", "year"
    
    # Application Info
    application_url = Column(String)
    applicants_count = Column(Integer, default=0)
    
    # ML Features
    cluster_id = Column(Integer, index=True)  # Assigned cluster
    embedding = Column(JSON)  # Job description embedding
    
    # Status
    is_active = Column(Boolean, default=True)

    # Professional taxonomy classification
    professional_field_id = Column(String, index=True, nullable=True)
    subfield_id = Column(String, index=True, nullable=True)
    canonical_role_id = Column(String, index=True, nullable=True)

    # Original job listing verification
    listing_status = Column(String, default="unknown", nullable=False, index=True)
    application_deadline = Column(DateTime(timezone=True), nullable=True)
    status_verified_at = Column(DateTime(timezone=True), nullable=True)

    posted_at = Column(DateTime(timezone=True))
    scraped_at = Column(DateTime(timezone=True), server_default=func.now())
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    company = relationship("Company", back_populates="jobs")
    scores = relationship("UserScore", back_populates="job")

    applications = relationship("JobApplication", back_populates="job")
    saved_jobs = relationship("SavedJob", back_populates="job")
    role_associations = relationship(
        "JobRoleAssociation",
        back_populates="job",
        cascade="all, delete-orphan",
        passive_deletes=True
    )
    
class JobRoleAssociation(Base):
    __tablename__ = "job_role_associations"

    __table_args__ = (
        UniqueConstraint(
            "job_id",
            "canonical_role_id",
            name="uq_job_role_association"
        ),
    )

    id = Column(Integer, primary_key=True, index=True)

    job_id = Column(
        Integer,
        ForeignKey("jobs.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    canonical_role_id = Column(String, nullable=False, index=True)
    professional_field_id = Column(String, nullable=False, index=True)
    subfield_id = Column(String, nullable=True, index=True)
    
    #this is for the secondary cross field mapping of role to primary field and additional field
    additional_professional_field_ids = Column(JSON, nullable=True)

    match_type = Column(String, nullable=False)
    matched_term = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    job = relationship("Job", back_populates="role_associations")

class JobCluster(Base):
    __tablename__ = "job_clusters"
    
    id = Column(Integer, primary_key=True, index=True)
    cluster_id = Column(Integer, unique=True, index=True)
    centroid = Column(JSON)  # Cluster centroid embedding
    job_count = Column(Integer, default=0)
    
    # Cluster characteristics (for interpretability)
    top_keywords = Column(JSON)  # Most common keywords in this cluster
    avg_salary_min = Column(Float)
    avg_salary_max = Column(Float)
    common_job_types = Column(JSON)
    common_locations = Column(JSON)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Resume(Base):
    __tablename__ = "resumes"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # File Information
    filename = Column(String, nullable=False)
    original_filename = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    file_size = Column(Integer)
    file_type = Column(String)
    
    # Resume Content
    raw_text = Column(Text)
    parsed_data = Column(JSON)  # Structured data from Gemini
    
    # Resume Embeddings (for different sections)
    experience_embedding = Column(JSON)
    skills_embedding = Column(JSON)
    education_embedding = Column(JSON)
    projects_embedding = Column(JSON)
    certifications_embedding = Column(JSON)
    
    # Metadata
    is_primary = Column(Boolean, default=False)
    target_job_title = Column(String)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="resumes")

class UserScore(Base):
    __tablename__ = "user_scores"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=True)  # Null for cluster scores
    cluster_id = Column(Integer, nullable=True)  # Null for individual job scores
    
    # Individual Section Scores
    experience_score = Column(Float)
    skills_score = Column(Float)
    education_score = Column(Float)
    projects_score = Column(Float)
    certifications_score = Column(Float)
    
    # Final weighted score
    final_score = Column(Float, index=True)
    
    # Match type based on score
    match_type = Column(String)  # "GOOD MATCH", "STRONG MATCH", "PERFECT MATCH"
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="scores")
    job = relationship("Job", back_populates="scores")
    
    # Ensure unique constraint for user-job and user-cluster pairs
    __table_args__ = (
        UniqueConstraint('user_id', 'job_id', name='unique_user_job_score'),
        UniqueConstraint('user_id', 'cluster_id', name='unique_user_cluster_score'),
    )

class JobApplication(Base):
    __tablename__ = "job_applications"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))
    
    status = Column(String, default="applied")  # "applied", "viewed", "rejected", "interview", "offer"
    applied_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Add these relationships
    user = relationship("User", back_populates="applications")
    job = relationship("Job", back_populates="applications")
    
    # Unique constraint to prevent duplicate applications
    __table_args__ = (
        UniqueConstraint('user_id', 'job_id', name='unique_user_job_application'),
    )
class SavedJob(Base):
    __tablename__ = "saved_jobs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))
    
    saved_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Add these relationships
    user = relationship("User", back_populates="saved_jobs")
    job = relationship("Job", back_populates="saved_jobs")
    
    # Unique constraint to prevent duplicate saves
    __table_args__ = (
        UniqueConstraint('user_id', 'job_id', name='unique_user_saved_job'),
    )