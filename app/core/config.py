from pydantic_settings import BaseSettings
from typing import Optional
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/careerpilotai")
    
    # JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here-change-in-production")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    # Google Gemini
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    
    # File upload
    MAX_FILE_SIZE: int = int(os.getenv("MAX_FILE_SIZE", str(10 * 1024 * 1024)))  # 10MB default
    UPLOAD_DIR: str = os.getenv("UPLOAD_DIR", "uploads")
    
    # ML Models
    EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    NUM_CLUSTERS: int = int(os.getenv("NUM_CLUSTERS", "1000"))
    
    # Scoring weights
    EXPERIENCE_WEIGHT: float = float(os.getenv("EXPERIENCE_WEIGHT", "0.3"))
    SKILLS_WEIGHT: float = float(os.getenv("SKILLS_WEIGHT", "0.25"))
    EDUCATION_WEIGHT: float = float(os.getenv("EDUCATION_WEIGHT", "0.2"))
    PROJECTS_WEIGHT: float = float(os.getenv("PROJECTS_WEIGHT", "0.15"))
    CERTIFICATIONS_WEIGHT: float = float(os.getenv("CERTIFICATIONS_WEIGHT", "0.1"))
    
    class Config:
        env_file = ".env"

settings = Settings()