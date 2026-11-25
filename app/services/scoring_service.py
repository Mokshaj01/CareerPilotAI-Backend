from sqlalchemy.orm import Session
from typing import Dict, List, Optional
import logging

from app.models import User, Resume, Job, JobCluster, UserScore
from app.services.embedding_service import embedding_service
from app.core.config import settings

logger = logging.getLogger(__name__)

class ScoringService:
    def __init__(self):
        self.embedding_service = embedding_service
    
    
    def calculate_user_job_scores(self, db: Session, user_id: int, resume_id: Optional[int] = None) -> bool:
        """Calculate scores for all job clusters for a user.

        Returns True only when all cluster scores are processed successfully.
        """
        # Get user's primary resume or specified resume
        if resume_id:
            resume = db.query(Resume).filter(
                Resume.id == resume_id,
                Resume.user_id == user_id
            ).first()
        else:
            resume = db.query(Resume).filter(
                Resume.user_id == user_id,
                Resume.is_primary == True
            ).first()

        if not resume:
            logger.warning("No resume found for user %s", user_id)
            return False

        # Get all job clusters
        clusters = db.query(JobCluster).all()

        if not clusters:
            logger.warning("No job clusters found. Please run clustering first.")
            return False

        failed_clusters = []

        # Isolate each cluster's changes with a savepoint.
        for cluster in clusters:
            try:
                with db.begin_nested():
                    self._calculate_cluster_score(
                        db, user_id, resume, cluster
                    )
                    # Flush inside the savepoint so database errors are
                    # raised before this cluster is considered successful.
                    db.flush()
            except Exception:
                failed_clusters.append(cluster.cluster_id)
                logger.exception(
                    "Error calculating score for cluster %s for user %s.",
                    cluster.cluster_id,
                    user_id,
                )

        # Commit successful cluster changes together.
        try:
            db.commit()
        except Exception:
            db.rollback()
            logger.exception(
                "Failed to commit job-match scores for user %s.",
                user_id,
            )
            raise

        if failed_clusters:
            logger.warning(
                "Score recalculation for user %s completed with failures "
                "in %s cluster(s): %s",
                user_id,
                len(failed_clusters),
                failed_clusters,
            )
            return False

        logger.info(
            "Score recalculation completed successfully for user %s.",
            user_id,
        )
        return True
 
 
    def _calculate_cluster_score(self, db: Session, user_id: int, resume: Resume, cluster: JobCluster) -> None:
        """Calculate score for a specific cluster"""
        # Check if score already exists
        existing_score = db.query(UserScore).filter(
            UserScore.user_id == user_id,
            UserScore.cluster_id == cluster.cluster_id
        ).first()
        
        if existing_score:
            # Update existing score
            self._update_score_values(existing_score, resume, cluster)
        else:
            # Create new score
            score = UserScore(
                user_id=user_id,
                cluster_id=cluster.cluster_id
            )
            self._update_score_values(score, resume, cluster)
            db.add(score)
    
    def _update_score_values(self, score: UserScore, resume: Resume, cluster: JobCluster) -> None:
        """Update score values based on resume and cluster"""
        cluster_centroid = cluster.centroid
        
        # Calculate individual section scores
        if resume.experience_embedding:
            score.experience_score = self.embedding_service.calculate_section_score(
                resume.experience_embedding, cluster_centroid
            )
        else:
            score.experience_score = 0.0
        
        if resume.skills_embedding:
            score.skills_score = self.embedding_service.calculate_section_score(
                resume.skills_embedding, cluster_centroid
            )
        else:
            score.skills_score = 0.0
        
        if resume.education_embedding:
            score.education_score = self.embedding_service.calculate_section_score(
                resume.education_embedding, cluster_centroid
            )
        else:
            score.education_score = 0.0
        
        if resume.projects_embedding:
            score.projects_score = self.embedding_service.calculate_section_score(
                resume.projects_embedding, cluster_centroid
            )
        else:
            score.projects_score = 0.0
        
        if resume.certifications_embedding:
            score.certifications_score = self.embedding_service.calculate_section_score(
                resume.certifications_embedding, cluster_centroid
            )
        else:
            score.certifications_score = 0.0
        
        # Calculate weighted final score
        section_scores = {
            'experience': score.experience_score,
            'skills': score.skills_score,
            'education': score.education_score,
            'projects': score.projects_score,
            'certifications': score.certifications_score
        }
        
        score.final_score = self.embedding_service.calculate_weighted_score(section_scores)
        score.match_type = self.embedding_service.get_match_type(score.final_score)
    
    def get_user_job_scores(self, db: Session, user_id: int, 
                           limit: int = 10, offset: int = 0) -> List[Dict]:
        """Get job scores for a user with job details"""
        # Get cluster scores for the user
        cluster_scores = db.query(UserScore).filter(
            UserScore.user_id == user_id,
            UserScore.cluster_id.isnot(None)
        ).order_by(UserScore.final_score.desc()).all()
        
        jobs_with_scores = []
        seen_jobs = set()
        
        for cluster_score in cluster_scores:
            # Get jobs in this cluster
            cluster_jobs = db.query(Job).filter(
                Job.cluster_id == cluster_score.cluster_id,
                Job.is_active == True
            ).limit(5).all()  # Limit jobs per cluster to avoid overwhelming results
            
            for job in cluster_jobs:
                if job.id not in seen_jobs and len(jobs_with_scores) < limit + offset:
                    jobs_with_scores.append({
                        'job': job,
                        'score': cluster_score
                    })
                    seen_jobs.add(job.id)
        
        # Apply pagination
        return jobs_with_scores[offset:offset + limit]
    
    def calculate_job_cluster_assignment(self, db: Session, job: Job) -> int:
        """Assign a job to a cluster based on its description"""
        if not job.description:
            logger.warning(f"Job {job.id} has no description for clustering")
            return 0  # Default cluster
        
        # Generate embedding for job description
        job_embedding = self.embedding_service.generate_embedding(job.description)
        
        # Store embedding in job
        job.embedding = job_embedding
        
        # Predict cluster
        try:
            cluster_id = self.embedding_service.predict_job_cluster(job_embedding)
            return cluster_id
        except ValueError as e:
            logger.error(f"Error predicting cluster for job {job.id}: {str(e)}")
            return 0  # Default cluster
    
    def update_cluster_statistics(self, db: Session, cluster_id: int) -> None:
        """Update statistics for a job cluster"""
        cluster = db.query(JobCluster).filter(
            JobCluster.cluster_id == cluster_id
        ).first()
        
        if not cluster:
            return
        
        # Get all jobs in this cluster
        cluster_jobs = db.query(Job).filter(
            Job.cluster_id == cluster_id,
            Job.is_active == True
        ).all()
        
        # Update job count
        cluster.job_count = len(cluster_jobs)
        
        # Calculate average salaries
        salaries_min = [job.salary_min for job in cluster_jobs if job.salary_min]
        salaries_max = [job.salary_max for job in cluster_jobs if job.salary_max]
        
        if salaries_min:
            cluster.avg_salary_min = sum(salaries_min) / len(salaries_min)
        
        if salaries_max:
            cluster.avg_salary_max = sum(salaries_max) / len(salaries_max)
        
        # Get common job types and locations
        job_types = [job.job_type for job in cluster_jobs if job.job_type]
        locations = [job.location for job in cluster_jobs if job.location]
        
        # Count frequencies and get top ones
        from collections import Counter
        
        job_type_counts = Counter(job_types)
        location_counts = Counter(locations)
        
        cluster.common_job_types = [jt for jt, _ in job_type_counts.most_common(5)]
        cluster.common_locations = [loc for loc, _ in location_counts.most_common(5)]
        
        db.commit()
    
    def recalculate_user_scores_for_cluster(self, db: Session, cluster_id: int) -> None:
        """Recalculate all user scores for a specific cluster when it's updated"""
        # Get all users who have scores for this cluster
        user_scores = db.query(UserScore).filter(
            UserScore.cluster_id == cluster_id
        ).all()
        
        cluster = db.query(JobCluster).filter(
            JobCluster.cluster_id == cluster_id
        ).first()
        
        if not cluster:
            return
        
        for user_score in user_scores:
            user = db.query(User).filter(User.id == user_score.user_id).first()
            if not user:
                continue
            
            # Get user's primary resume
            resume = db.query(Resume).filter(
                Resume.user_id == user.id,
                Resume.is_primary == True
            ).first()
            
            if not resume:
                continue
            
            # Recalculate scores
            self._update_score_values(user_score, resume, cluster)
        
        db.commit()

# Initialize scoring service
scoring_service = ScoringService()