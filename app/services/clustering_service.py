from sqlalchemy.orm import Session
from typing import List, Dict
import logging
from collections import Counter
import numpy as np

from app.models import Job, JobCluster
from app.services.embedding_service import embedding_service
from app.core.config import settings

logger = logging.getLogger(__name__)

def convert_numpy_int(value):
    """Convert numpy integers to Python int for database compatibility"""
    if isinstance(value, (np.integer, np.int32, np.int64)):
        return int(value.item())
    return int(value)

class ClusteringService:
    def __init__(self):
        self.embedding_service = embedding_service
    
    def initialize_job_clustering(self, db: Session) -> bool:
        """Initialize job clustering with existing jobs"""
        try:
            # Get all active jobs
            jobs = db.query(Job).filter(
                Job.is_active == True
            ).all()
            
            # Generate embeddings only for jobs with usable attributes
            eligible_jobs = []
            embeddings = []
            skipped_jobs = []

            for job in jobs:
                try:
                    embedding = (
                        self.embedding_service.generate_job_clustering_embedding(job)
                    )
                    eligible_jobs.append(job)
                    embeddings.append(embedding)

                except ValueError as e:
                    logger.warning(
                        f"Skipping job ID {job.id}: {str(e)}"
                    )
                    skipped_jobs.append(job)

            if len(eligible_jobs) < 10:
                logger.warning(
                    f"Not enough eligible jobs for clustering. "
                    f"Found {len(eligible_jobs)}, need at least 10."
                )
                return False

            logger.info(
                f"Initializing clustering with {len(eligible_jobs)} eligible jobs"
            )

            # Update job embeddings in database
            for job, embedding in zip(eligible_jobs, embeddings):
                job.embedding = embedding
            
            # Train clustering model
            cluster_labels = self.embedding_service.train_job_clusters(embeddings)
            
            # Convert numpy integers to Python integers
            cluster_labels = [convert_numpy_int(c) for c in cluster_labels]
            
            # Assign cluster IDs to jobs
            for job, cluster_id in zip(eligible_jobs, cluster_labels):
                job.cluster_id = convert_numpy_int(cluster_id)
                
            # Clear stale clustering data for jobs without usable attributes
            for job in skipped_jobs:
                job.embedding = None
                job.cluster_id = None    
            
            db.commit()
            
            # Create cluster records
            self._create_cluster_records(db, cluster_labels)
            
            # Update cluster statistics
            self.update_all_cluster_statistics(db)
            
            logger.info("Job clustering initialization completed successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error initializing job clustering: {str(e)}")
            db.rollback()
            return False
    
    def _create_cluster_records(self, db: Session, cluster_labels: List[int]) -> None:
        """Create JobCluster records for each cluster"""
        unique_clusters = set(cluster_labels)
        
        for cluster_id in unique_clusters:
            cluster_id = convert_numpy_int(cluster_id)
            
            # Check if cluster already exists
            existing_cluster = db.query(JobCluster).filter(
                JobCluster.cluster_id == cluster_id
            ).first()
            
            if not existing_cluster:
                # Get centroid from embedding service
                centroid = self.embedding_service.get_cluster_centroid(cluster_id)
                
                cluster = JobCluster(
                    cluster_id=cluster_id,
                    centroid=centroid,
                    job_count=0,
                    top_keywords=[],
                    common_job_types=[],
                    common_locations=[]
                )

                db.add(cluster)
        
        db.commit()
    
   
    def recalculate_job_clusters(self, db: Session) -> bool:
        """Recalculate job clusters with current jobs"""
        try:
            logger.info("Starting job cluster recalculation...")

            # Get all active jobs
            jobs = db.query(Job).filter(
                Job.is_active == True
            ).all()

            # Generate embeddings only for jobs with usable attributes
            eligible_jobs = []
            all_embeddings = []
            skipped_jobs = []

            for job in jobs:
                try:
                    embedding = (
                        self.embedding_service.generate_job_clustering_embedding(job)
                    )
                    eligible_jobs.append(job)
                    all_embeddings.append(embedding)

                except ValueError as e:
                    logger.warning(
                        f"Skipping job ID {job.id}: {str(e)}"
                    )
                    skipped_jobs.append(job)

            if len(eligible_jobs) < 10:
                logger.warning(
                    f"Not enough eligible jobs for reclustering. "
                    f"Found {len(eligible_jobs)}, need at least 10."
                )
                return False

            logger.info(
                f"Recalculating clusters for {len(eligible_jobs)} eligible jobs"
            )

            # Update all eligible job embeddings
            for job, embedding in zip(eligible_jobs, all_embeddings):
                job.embedding = embedding

            # Retrain clustering with consistent multi-attribute embeddings
            cluster_labels = self.embedding_service.train_job_clusters(
                all_embeddings
            )

            # Convert numpy integers to Python integers
            cluster_labels = [
                convert_numpy_int(c) for c in cluster_labels
            ]

            # Update eligible job cluster assignments
            for job, cluster_id in zip(eligible_jobs, cluster_labels):
                job.cluster_id = convert_numpy_int(cluster_id)

            # Clear stale clustering data for jobs without usable attributes
            for job in skipped_jobs:
                job.embedding = None
                job.cluster_id = None

            db.commit()

            # Update cluster records
            self._update_cluster_records(db, cluster_labels)

            # Update statistics
            self.update_all_cluster_statistics(db)

            logger.info("Job cluster recalculation completed successfully")
            return True

        except Exception as e:
            logger.error(f"Error recalculating job clusters: {str(e)}")
            db.rollback()
            return False

    def _update_cluster_records(self, db: Session, cluster_labels: List[int]) -> None:
        """Update existing cluster records or create new ones"""
        unique_clusters = set(cluster_labels)
        
        # Get existing clusters
        existing_clusters = {
            cluster.cluster_id: cluster 
            for cluster in db.query(JobCluster).all()
        }
        
        for cluster_id in unique_clusters:
            cluster_id = convert_numpy_int(cluster_id)
            
            if cluster_id in existing_clusters:
                # Update existing cluster centroid
                centroid = self.embedding_service.get_cluster_centroid(cluster_id)
                existing_clusters[cluster_id].centroid = centroid
            else:
                # Create new cluster
                centroid = self.embedding_service.get_cluster_centroid(cluster_id)
                cluster = JobCluster(
                    cluster_id=cluster_id,
                    centroid=centroid,
                    job_count=0,
                    top_keywords=[],
                    common_job_types=[],
                    common_locations=[]
                )
                db.add(cluster)
        
        # Remove clusters that no longer exist
        for existing_cluster_id, cluster in existing_clusters.items():
            if existing_cluster_id not in unique_clusters:
                db.delete(cluster)
        
        db.commit()
    
    def update_all_cluster_statistics(self, db: Session) -> None:
        """Update statistics for all clusters"""
        clusters = db.query(JobCluster).all()
        
        for cluster in clusters:
            self._update_cluster_statistics(db, cluster)
        
        db.commit()
    
    def _update_cluster_statistics(self, db: Session, cluster: JobCluster) -> None:
        """Update statistics for a specific cluster"""
        # Get all jobs in this cluster
        cluster_jobs = db.query(Job).filter(
            Job.cluster_id == cluster.cluster_id,
            Job.is_active == True
        ).all()
        
        # Update job count
        cluster.job_count = len(cluster_jobs)
        
        if not cluster_jobs:
            return
        
        # Calculate salary statistics
        salaries_min = [job.salary_min for job in cluster_jobs if job.salary_min]
        salaries_max = [job.salary_max for job in cluster_jobs if job.salary_max]
        
        cluster.avg_salary_min = sum(salaries_min) / len(salaries_min) if salaries_min else None
        cluster.avg_salary_max = sum(salaries_max) / len(salaries_max) if salaries_max else None
        
        # Get common job types and locations
        job_types = [job.job_type for job in cluster_jobs if job.job_type]
        locations = [job.location for job in cluster_jobs if job.location]
        
        job_type_counts = Counter(job_types)
        location_counts = Counter(locations)
        
        cluster.common_job_types = [jt for jt, _ in job_type_counts.most_common(5)]
        cluster.common_locations = [loc for loc, _ in location_counts.most_common(5)]
        
        # Extract top keywords from job descriptions
        cluster.top_keywords = self._extract_top_keywords(cluster_jobs)
    
    def _extract_top_keywords(self, jobs: List[Job]) -> List[str]:
        """Extract top keywords from job descriptions in a cluster"""
        # Combine all job descriptions
        all_text = " ".join([job.description or "" for job in jobs])
        
        # Simple keyword extraction (you might want to use more sophisticated NLP)
        import re
        from collections import Counter
        
        # Common technical keywords to look for
        tech_keywords = [
            "python", "java", "javascript", "react", "angular", "node.js",
            "machine learning", "deep learning", "tensorflow", "pytorch",
            "sql", "mongodb", "postgresql", "aws", "azure", "gcp",
            "docker", "kubernetes", "microservices", "api", "rest",
            "agile", "scrum", "git", "ci/cd", "devops", "cloud",
            "artificial intelligence", "ai", "ml", "nlp", "computer vision",
            "data science", "analytics", "statistics", "algorithms"
        ]
        
        text_lower = all_text.lower()
        found_keywords = []
        
        for keyword in tech_keywords:
            if keyword in text_lower:
                # Count occurrences
                count = len(re.findall(r'\b' + re.escape(keyword) + r'\b', text_lower))
                found_keywords.extend([keyword] * count)
        
        # Get most common keywords
        keyword_counts = Counter(found_keywords)
        return [kw for kw, _ in keyword_counts.most_common(10)]
    
    def assign_job_to_cluster(self, db: Session, job: Job) -> int:
        """Assign a single job to the most appropriate cluster."""

        try:
            # Generate a multi-attribute embedding
            job_embedding = (
                self.embedding_service.generate_job_clustering_embedding(job)
            )

            # Store the new embedding
            job.embedding = job_embedding

            # Predict cluster using the trained K-means model
            cluster_id = self.embedding_service.predict_job_cluster(
                job_embedding
            )

            job.cluster_id = convert_numpy_int(cluster_id)

            # Update cluster statistics
            cluster = db.query(JobCluster).filter(
                JobCluster.cluster_id == job.cluster_id
            ).first()

            if cluster:
                self._update_cluster_statistics(db, cluster)

            return job.cluster_id

        except ValueError as e:
            logger.warning(
                f"Unable to assign job to cluster: {str(e)}"
            )
            return 0

        except Exception as e:
            logger.error(
                f"Error assigning job to cluster: {str(e)}"
            )
            return 0
        
# Initialize clustering service
clustering_service = ClusteringService()