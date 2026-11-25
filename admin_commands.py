"""
Admin commands for managing the NextAI Career backend.
Run these commands to initialize the system.
"""

import asyncio
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base
from app.services.clustering_service import clustering_service
from app.services.job_scraper import job_service
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_tables():
    """Create all database tables"""
    logger.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully")

def initialize_job_clustering():
    """Initialize job clustering with existing data"""
    logger.info("Initializing job clustering...")
    db = SessionLocal()
    try:
        success = clustering_service.initialize_job_clustering(db)
        if success:
            logger.info("Job clustering initialized successfully")
        else:
            logger.warning("Job clustering initialization failed or insufficient data")
    except Exception as e:
        logger.error(f"Error initializing job clustering: {str(e)}")
    finally:
        db.close()

def scrape_initial_jobs():
    """Scrape initial batch of jobs from LinkedIn"""
    logger.info("Starting initial job scraping...")
    db = SessionLocal()
    try:
        jobs_added = job_service.scrape_and_store_jobs(db)
        logger.info(f"Initial scraping completed. Added {jobs_added} jobs.")
    except Exception as e:
        logger.error(f"Error in initial job scraping: {str(e)}")
    finally:
        db.close()

def setup_initial_data():
    """Setup initial data for the system"""
    logger.info("Setting up initial data...")
    
    # Create sample companies
    db = SessionLocal()
    try:
        from app.models import Company
        
        sample_companies = [
            {
                "name": "Google",
                "industry": "Technology",
                "company_size": "10000+",
                "headquarters": "Mountain View, CA",
                "website_url": "https://google.com",
                "stage": "Public Company"
            },
            {
                "name": "Microsoft",
                "industry": "Technology", 
                "company_size": "10000+",
                "headquarters": "Redmond, WA",
                "website_url": "https://microsoft.com",
                "stage": "Public Company"
            },
            {
                "name": "OpenAI",
                "industry": "Artificial Intelligence",
                "company_size": "201-500",
                "headquarters": "San Francisco, CA", 
                "website_url": "https://openai.com",
                "stage": "Late Stage"
            },
            {
                "name": "Anthropic",
                "industry": "Artificial Intelligence",
                "company_size": "51-200",
                "headquarters": "San Francisco, CA",
                "website_url": "https://anthropic.com", 
                "stage": "Early Stage"
            }
        ]
        
        for company_data in sample_companies:
            existing = db.query(Company).filter(Company.name == company_data["name"]).first()
            if not existing:
                company = Company(**company_data)
                db.add(company)
        
        db.commit()
        logger.info("Sample companies added successfully")
        
    except Exception as e:
        logger.error(f"Error setting up initial data: {str(e)}")
    finally:
        db.close()

def full_system_setup():
    """Complete system setup - run this for initial deployment"""
    logger.info("Starting full system setup...")
    
    # Step 1: Create database tables
    create_tables()
    
    # Step 2: Setup initial data
    setup_initial_data()
    
    # Step 3: Scrape initial jobs
    scrape_initial_jobs()
    
    # Step 4: Initialize clustering
    initialize_job_clustering()
    
    logger.info("Full system setup completed!")

def recalculate_all_clusters():
    """Recalculate all job clusters"""
    logger.info("Recalculating all job clusters...")
    db = SessionLocal()
    try:
        success = clustering_service.recalculate_job_clusters(db)
        if success:
            logger.info("Job clusters recalculated successfully")
        else:
            logger.warning("Job cluster recalculation failed")
    except Exception as e:
        logger.error(f"Error recalculating clusters: {str(e)}")
    finally:
        db.close()

def update_cluster_statistics():
    """Update statistics for all clusters"""
    logger.info("Updating cluster statistics...")
    db = SessionLocal()
    try:
        clustering_service.update_all_cluster_statistics(db)
        logger.info("Cluster statistics updated successfully")
    except Exception as e:
        logger.error(f"Error updating cluster statistics: {str(e)}")
    finally:
        db.close()

def cleanup_inactive_jobs():
    """Mark old jobs as inactive"""
    logger.info("Cleaning up old jobs...")
    from datetime import datetime, timedelta
    from app.models import Job
    
    db = SessionLocal()
    try:
        cutoff_date = datetime.now() - timedelta(days=30)
        
        updated_count = db.query(Job).filter(
            Job.posted_at < cutoff_date,
            Job.is_active == True
        ).update({"is_active": False})
        
        db.commit()
        logger.info(f"Marked {updated_count} old jobs as inactive")
        
    except Exception as e:
        logger.error(f"Error cleaning up jobs: {str(e)}")
    finally:
        db.close()

def get_system_stats():
    """Get system statistics"""
    db = SessionLocal()
    try:
        from app.models import User, Job, Company, Resume, JobCluster, UserScore
        
        stats = {
            "users": db.query(User).count(),
            "companies": db.query(Company).count(),
            "total_jobs": db.query(Job).count(),
            "active_jobs": db.query(Job).filter(Job.is_active == True).count(),
            "resumes": db.query(Resume).count(),
            "job_clusters": db.query(JobCluster).count(),
            "user_scores": db.query(UserScore).count()
        }
        
        logger.info("System Statistics:")
        for key, value in stats.items():
            logger.info(f"  {key}: {value}")
        
        return stats
        
    except Exception as e:
        logger.error(f"Error getting system stats: {str(e)}")
        return {}
    finally:
        db.close()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python admin_commands.py <command>")
        print("Available commands:")
        print("  - create_tables: Create database tables")
        print("  - setup_data: Setup initial data")
        print("  - scrape_jobs: Scrape initial jobs from LinkedIn")
        print("  - init_clustering: Initialize job clustering")
        print("  - full_setup: Complete system setup")
        print("  - recalculate_clusters: Recalculate job clusters")
        print("  - update_stats: Update cluster statistics")
        print("  - cleanup_jobs: Mark old jobs as inactive")
        print("  - system_stats: Show system statistics")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "create_tables":
        create_tables()
    elif command == "setup_data":
        setup_initial_data()
    elif command == "scrape_jobs":
        scrape_initial_jobs()
    elif command == "init_clustering":
        initialize_job_clustering()
    elif command == "full_setup":
        full_system_setup()
    elif command == "recalculate_clusters":
        recalculate_all_clusters()
    elif command == "update_stats":
        update_cluster_statistics()
    elif command == "cleanup_jobs":
        cleanup_inactive_jobs()
    elif command == "system_stats":
        get_system_stats()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)