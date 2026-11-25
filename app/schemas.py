from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict, Any
from datetime import datetime
# User Schemas
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str

class GoogleAuthRequest(BaseModel):
    access_token: str
    
class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# User Profile Schemas
class UserProfileCreate(BaseModel):
    phone: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    location: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    portfolio_url: Optional[str] = None
    summary: Optional[str] = None
    experience: Optional[List[Dict[str, Any]]] = None
    skills: Optional[List[str]] = None
    education: Optional[List[Dict[str, Any]]] = None
    projects: Optional[List[Dict[str, Any]]] = None
    certifications: Optional[List[Dict[str, Any]]] = None
    languages: Optional[List[Dict[str, Any]]] = None
    preferred_job_types: Optional[List[str]] = None
    preferred_locations: Optional[List[str]] = None
    salary_expectation_min: Optional[int] = None
    salary_expectation_max: Optional[int] = None

# Company Schemas
class CompanyCreate(BaseModel):
    name: str
    linkedin_id: Optional[str] = None
    description: Optional[str] = None
    industry: Optional[str] = None
    company_size: Optional[str] = None
    headquarters: Optional[str] = None
    website_url: Optional[str] = None
    logo_url: Optional[str] = None
    stage: Optional[str] = None

# Job Schemas
class JobCreate(BaseModel):
    company_id: int
    linkedin_job_id: Optional[str] = None
    title: str
    description: Optional[str] = None
    requirements: Optional[str] = None
    benefits: Optional[str] = None
    location: Optional[str] = None
    location_type: Optional[str] = None
    job_type: Optional[str] = None
    experience_level: Optional[str] = None
    department: Optional[str] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    salary_currency: Optional[str] = "USD"
    salary_period: Optional[str] = "year"
    application_url: Optional[str] = None
    applicants_count: Optional[int] = 0
    posted_at: Optional[datetime] = None

# Resume Schemas
class ResumeUpload(BaseModel):
    target_job_title: Optional[str] = None

class ResumeResponse(BaseModel):
    id: int
    user_id: int
    filename: str
    original_filename: str
    file_size: int
    file_type: str
    is_primary: bool
    target_job_title: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True

class ParsedResumeData(BaseModel):
    personal_info: Dict[str, Any]
    experience: List[Dict[str, Any]]
    skills: List[str]
    education: List[Dict[str, Any]]
    projects: List[Dict[str, Any]]
    certifications: List[Dict[str, Any]]
    languages: List[Dict[str, Any]]

# User Score Schemas
class UserScoreResponse(BaseModel):
    id: int
    user_id: int
    job_id: Optional[int] = None
    cluster_id: Optional[int] = None
    experience_score: float
    skills_score: float
    education_score: float
    projects_score: float
    certifications_score: float
    final_score: float
    match_type: str
    created_at: datetime
    
    class Config:
        from_attributes = True

# Cluster Schemas
class JobClusterResponse(BaseModel):
    id: int
    cluster_id: int
    job_count: int
    top_keywords: List[str]
    avg_salary_min: Optional[float] = None
    avg_salary_max: Optional[float] = None
    common_job_types: List[str]
    common_locations: List[str]
    
    class Config:
        from_attributes = True
        

class PrimaryResumeInfo(BaseModel):
    id: int
    original_filename: str
    target_job_title: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    parsed_data: Optional[Dict[str, Any]] = None

class UserProfileResponse(BaseModel):
    id: int
    user_id: int
    
    # Personal Information
    phone: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    location: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    portfolio_url: Optional[str] = None
    
    # Professional Summary
    summary: Optional[str] = None
    
    # Experience, Skills, Education, etc.
    experience: Optional[List[Dict[str, Any]]] = None
    skills: Optional[List[str]] = None
    education: Optional[List[Dict[str, Any]]] = None
    projects: Optional[List[Dict[str, Any]]] = None
    certifications: Optional[List[Dict[str, Any]]] = None
    languages: Optional[List[Dict[str, Any]]] = None
    
    # Job Preferences
    preferred_job_types: Optional[List[str]] = None
    preferred_locations: Optional[List[str]] = None
    salary_expectation_min: Optional[int] = None
    salary_expectation_max: Optional[int] = None
    
    # Primary Resume Info
    primary_resume: Optional[PrimaryResumeInfo] = None
    
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class ResumeStatsResponse(BaseModel):
    id: int
    original_filename: str
    is_primary: bool
    target_job_title: Optional[str] = None
    created_at: datetime
    has_embeddings: bool

class ProfileResumeStatsResponse(BaseModel):
    total_resumes: int
    primary_resume_id: Optional[int] = None
    resumes: List[ResumeStatsResponse]

# Company schemas
class CompanyBase(BaseModel):
    name: str
    description: Optional[str] = None
    industry: Optional[str] = None
    company_size: Optional[str] = None
    headquarters: Optional[str] = None
    website_url: Optional[str] = None
    logo_url: Optional[str] = None
    stage: Optional[str] = None

class CompanyResponse(CompanyBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class CompanyBasic(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

# Job schemas
class JobBase(BaseModel):
    title: str
    description: Optional[str] = None
    requirements: Optional[str] = None
    benefits: Optional[str] = None
    location: Optional[str] = None
    location_type: Optional[str] = None
    job_type: Optional[str] = None
    experience_level: Optional[str] = None
    department: Optional[str] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    salary_currency: Optional[str] = "USD"
    salary_period: Optional[str] = "year"
    application_url: Optional[str] = None
    applicants_count: Optional[int] = 0

class JobResponse(JobBase):
    id: int
    company_id: Optional[int] = None
    platform_job_id: Optional[str] = None
    platform: Optional[str] = None
    cluster_id: Optional[int] = None
    is_active: Optional[bool] = True
    # Professional taxonomy classification
    professional_field_id: Optional[str] = None
    subfield_id: Optional[str] = None
    canonical_role_id: Optional[str] = None

    # Original listing verification
    listing_status: Optional[str] = "unknown"
    application_deadline: Optional[datetime] = None
    status_verified_at: Optional[datetime] = None

    posted_at: Optional[datetime] = None
    scraped_at: Optional[datetime] = None
    created_at: datetime
    company: Optional[CompanyResponse] = None
    
    class Config:
        from_attributes = True

class JobBasic(BaseModel):
    id: int
    title: str
    company: CompanyBasic
    location: Optional[str] = None
    job_type: Optional[str] = None
    posted_at: Optional[datetime] = None
    created_at: datetime

class JobWithScore(JobResponse):
    match_score: Optional[float] = None
    match_type: Optional[str] = None
    experience_score: Optional[float] = None
    skills_score: Optional[float] = None
    education_score: Optional[float] = None
    projects_score: Optional[float] = None
    certifications_score: Optional[float] = None
    # Optional fields for applied/saved job details
    application: Optional[Dict[str, Any]] = None
    saved: Optional[Dict[str, Any]] = None

# Job filters
class JobFilters(BaseModel):
    location: Optional[List[str]] = None
    job_type: Optional[List[str]] = None
    experience_level: Optional[List[str]] = None
    department: Optional[List[str]] = None
    company: Optional[List[str]] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    geographic_scope: Optional[str] = None
    location_type: Optional[List[str]] = None
    # Professional taxonomy hierarchy
    professional_field_ids: Optional[List[str]] = None
    subfield_ids: Optional[List[str]] = None
    canonical_role_ids: Optional[List[str]] = None

# Job search response
class JobSearchResponse(BaseModel):
    jobs: List[JobWithScore]
    total: int
    page: int
    total_pages: int
    filters: Dict[str, List[str]]

# Job application schemas
class JobApplicationCreate(BaseModel):
    job_id: int

class JobApplicationResponse(BaseModel):
    id: int
    user_id: int
    job_id: int
    status: str = "applied"
    applied_at: datetime
    
    class Config:
        from_attributes = True

# Saved job schemas
class SavedJobCreate(BaseModel):
    job_id: int

class SavedJobResponse(BaseModel):
    id: int
    user_id: int
    job_id: int
    saved_at: datetime
    job: Optional[JobBasic] = None
    
    class Config:
        from_attributes = True
