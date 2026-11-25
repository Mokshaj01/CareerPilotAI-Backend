from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import uvicorn

from app.database import engine, get_db
from app.models import Base
from app.routers import auth, users, jobs, resumes, companies, taxonomy
from app.core.config import settings
from app.services.scheduler import start_scheduler

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CareerPilotAI Backend",
    description="Backend API for CareerPilotAI",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["authentication"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(jobs.router, prefix="/api/jobs", tags=["jobs"])
app.include_router(resumes.router, prefix="/api/resumes", tags=["resumes"])
app.include_router(companies.router, prefix="/api/companies", tags=["companies"])
app.include_router(taxonomy.router, prefix="/api/taxonomy", tags=["taxonomy"])

@app.on_event("startup")
async def startup_event():
    """Initialize services on startup"""
    start_scheduler()

@app.get("/")
async def root():
    return {"message": "NextAI Career Backend API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )