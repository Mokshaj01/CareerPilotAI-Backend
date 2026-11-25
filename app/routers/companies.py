from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.models import Company, Job, User
from app.schemas import CompanyResponse, CompanyCreate, JobResponse
from app.services.auth import get_current_user

router = APIRouter()

@router.get("/", response_model=List[CompanyResponse])
async def get_companies(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    search: Optional[str] = Query(None),
    industry: Optional[str] = Query(None),
    stage: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    """Get list of companies with optional filters"""
    query = db.query(Company)
    
    if search:
        query = query.filter(Company.name.ilike(f"%{search}%"))
    
    if industry:
        query = query.filter(Company.industry == industry)
    
    if stage:
        query = query.filter(Company.stage == stage)
    
    companies = query.offset(skip).limit(limit).all()
    return companies

@router.get("/{company_id}", response_model=CompanyResponse)
async def get_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    """Get company details"""
    company = db.query(Company).filter(Company.id == company_id).first()
    
    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found"
        )
    
    return company

@router.get("/{company_id}/jobs", response_model=List[JobResponse])
async def get_company_jobs(
    company_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    active_only: bool = Query(True),
    db: Session = Depends(get_db)
):
    """Get jobs for a specific company"""
    # Verify company exists
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found"
        )
    
    query = db.query(Job).filter(Job.company_id == company_id)
    
    if active_only:
        query = query.filter(Job.is_active == True)
    
    jobs = query.offset(skip).limit(limit).all()
    return jobs

@router.post("/", response_model=CompanyResponse)
async def create_company(
    company_data: CompanyCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new company (admin only functionality)"""
    # In a real app, you'd check if user is admin
    
    # Check if company already exists
    existing_company = db.query(Company).filter(
        Company.name == company_data.name
    ).first()
    
    if existing_company:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Company with this name already exists"
        )
    
    company = Company(**company_data.dict())
    db.add(company)
    db.commit()
    db.refresh(company)
    
    return company

@router.get("/stats/industries")
async def get_industry_stats(db: Session = Depends(get_db)):
    """Get statistics about company industries"""
    from sqlalchemy import func
    
    industry_stats = db.query(
        Company.industry,
        func.count(Company.id).label('count')
    ).group_by(Company.industry).all()
    
    return [
        {"industry": stat.industry, "count": stat.count}
        for stat in industry_stats if stat.industry
    ]

@router.get("/stats/stages")
async def get_stage_stats(db: Session = Depends(get_db)):
    """Get statistics about company stages"""
    from sqlalchemy import func
    
    stage_stats = db.query(
        Company.stage,
        func.count(Company.id).label('count')
    ).group_by(Company.stage).all()
    
    return [
        {"stage": stat.stage, "count": stat.count}
        for stat in stage_stats if stat.stage
    ]

@router.get("/search/suggestions")
async def get_company_suggestions(
    q: str = Query(..., min_length=2),
    limit: int = Query(10, ge=1, le=20),
    db: Session = Depends(get_db)
):
    """Get company name suggestions for autocomplete"""
    suggestions = db.query(Company.name).filter(
        Company.name.ilike(f"%{q}%")
    ).limit(limit).all()
    
    return [name[0] for name in suggestions]