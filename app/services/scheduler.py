from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import logging
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Resume
from app.services.job_scraper import job_service
from app.services.clustering_service import clustering_service
from app.services.scoring_service import scoring_service

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()

def scrape_linkedin_jobs():
    """Scheduled job to scrape LinkedIn for new jobs"""
    logger.info("Starting scheduled LinkedIn job scraping...")
    
    db = SessionLocal()
    try:
        jobs_added = job_service.scrape_and_store_jobs(db)
        logger.info(f"Scheduled scraping completed. Added {jobs_added} new jobs.")
        
        # Update cluster statistics after adding new jobs
        if jobs_added > 0:
            clustering_service.update_all_cluster_statistics(db)
            
    except Exception as e:
        logger.error(f"Error in scheduled job scraping: {str(e)}")
    finally:
        db.close()

def recalculate_clusters():
    """Recalculate job clusters and refresh scores for primary resumes."""
    logger.info("Starting scheduled cluster recalculation...")

    db = SessionLocal()
    try:
        clusters_updated = clustering_service.recalculate_job_clusters(db)

        if not clusters_updated:
            logger.warning(
                "Cluster recalculation did not complete; skipping score recalculation."
            )
            return

        logger.info("Scheduled cluster recalculation completed successfully.")

        primary_resumes = db.query(Resume).filter(
            Resume.is_primary == True
        ).all()

        logger.info(
            "Recalculating job-match scores for %s primary resumes.",
            len(primary_resumes)
        )

       
        for resume in primary_resumes:
            try:
                scores_succeeded = scoring_service.calculate_user_job_scores(
                    db, resume.user_id, resume.id
                )

                if scores_succeeded:
                    logger.info(
                        "Processed job-match scores successfully for user %s "
                        "using primary resume %s.",
                        resume.user_id, resume.id
                    )
                else:
                    logger.warning(
                        "Job-match score recalculation was incomplete for "
                        "user %s using primary resume %s.",
                        resume.user_id, resume.id
                    )

            except Exception:
                db.rollback()
                logger.exception(
                    "Error recalculating job-match scores for user %s.",
                    resume.user_id
                )


    except Exception:
        db.rollback()
        logger.exception("Error in scheduled cluster recalculation.")
    finally:
        db.close()
def cleanup_old_jobs():
    """Remove jobs older than 30 days"""
    logger.info("Starting job cleanup...")
    
    from datetime import datetime, timedelta
    from app.models import Job
    
    db = SessionLocal()
    try:
        cutoff_date = datetime.now() - timedelta(days=30)
        
        # Mark old jobs as inactive instead of deleting them
        old_jobs = db.query(Job).filter(
            Job.posted_at < cutoff_date,
            Job.is_active == True
        ).update({"is_active": False})
        
        db.commit()
        logger.info(f"Marked {old_jobs} old jobs as inactive.")
        
    except Exception as e:
        logger.error(f"Error in job cleanup: {str(e)}")
    finally:
        db.close()

def start_scheduler():
    """Start the background scheduler with all scheduled jobs"""
    
    # Schedule LinkedIn job scraping every hour
    scheduler.add_job(
        func=scrape_linkedin_jobs,
        trigger=CronTrigger(minute=0),  # Every hour at minute 0
        id='linkedin_scraping',
        name='LinkedIn Job Scraping',
        replace_existing=True
    )
    
    # Schedule cluster recalculation every 6 hours
    scheduler.add_job(
        func=recalculate_clusters,
        trigger=CronTrigger(hour='*/6', minute=0),  # Every 6 hours
        id='cluster_recalculation',
        name='Job Cluster Recalculation',
        replace_existing=True
    )
    
    # Schedule job cleanup daily at 2 AM
    scheduler.add_job(
        func=cleanup_old_jobs,
        trigger=CronTrigger(hour=2, minute=0),  # Daily at 2 AM
        id='job_cleanup',
        name='Old Job Cleanup',
        replace_existing=True
    )
    
    scheduler.start()
    logger.info("Background scheduler started with scheduled jobs")

def stop_scheduler():
    """Stop the background scheduler"""
    scheduler.shutdown()
    logger.info("Background scheduler stopped")