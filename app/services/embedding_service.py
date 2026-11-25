from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Dict, Any
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

from app.core.config import settings
from app.data.job_taxonomy import (
    PROFESSIONAL_FIELDS,
    SUBFIELDS_BY_FIELD,
    CANONICAL_ROLES,
)

# Job clustering attribute weights
JOB_CLUSTERING_WEIGHTS = {
    "title": 0.20,
    "description": 0.35,
    "requirements": 0.15,
    "professional_field": 0.10,
    "subfield": 0.10,
    "canonical_role": 0.10,
}

JOB_CLUSTERING_EMBEDDING_VERSION = "multi_attribute_v1"

# Taxonomy lookup dictionaries
PROFESSIONAL_FIELD_NAMES = {
    field["id"]: field["name"]
    for field in PROFESSIONAL_FIELDS
}

SUBFIELD_NAMES = {
    (field_id, subfield["id"]): subfield["name"]
    for field_id, subfields in SUBFIELDS_BY_FIELD.items()
    for subfield in subfields
}

CANONICAL_ROLE_NAMES = {
    role["id"]: role["name"]
    for role in CANONICAL_ROLES
}

class EmbeddingService:
    def __init__(self):
        self.model = SentenceTransformer(settings.EMBEDDING_MODEL)
        self.kmeans_model = None
        self.cluster_centroids = None
        
    def generate_embedding(self, text: str) -> List[float]:
        """Generate embedding for given text"""
        if not text or not text.strip():
            # Return zero vector for empty text
            return [0.0] * self.model.get_sentence_embedding_dimension()
        
        embedding = self.model.encode(text)
        return embedding.tolist()
    
    def generate_job_attribute_embeddings(
        self,
        job: Any
    ) -> Dict[str, List[float]]:
        """Generate separate embeddings for available job attributes."""
        attributes = {}
        
        title = getattr(job, "title", None)
        description = getattr(job, "description", None)
        requirements = getattr(job, "requirements", None)

        professional_field_id = getattr(job, "professional_field_id", None)
        subfield_id = getattr(job, "subfield_id", None)
        canonical_role_id = getattr(job, "canonical_role_id", None)

        if title and str(title).strip():
            attributes["title"] = str(title).strip()

        if description and str(description).strip():
            attributes["description"] = str(description).strip()

        if requirements and str(requirements).strip():
            attributes["requirements"] = str(requirements).strip()

        field_name = PROFESSIONAL_FIELD_NAMES.get(professional_field_id)
        if field_name:
            attributes["professional_field"] = field_name

        subfield_name = SUBFIELD_NAMES.get(
            (professional_field_id, subfield_id)
        )
        if subfield_name:
            attributes["subfield"] = subfield_name

        role_name = CANONICAL_ROLE_NAMES.get(canonical_role_id)
        if role_name:
            attributes["canonical_role"] = role_name

        embeddings = {}

        for attribute, text in attributes.items():
            embedding = self.model.encode(text)
            embeddings[attribute] = embedding.tolist()

        return embeddings

    def generate_job_clustering_embedding(
        self,
        job: Any
    ) -> List[float]:
        """Generate a normalized weighted embedding for job clustering."""
        attribute_embeddings = self.generate_job_attribute_embeddings(job)

        if not attribute_embeddings:
            raise ValueError(
                "Cannot generate job clustering embedding: "
                "no usable job attributes found."
            )

        available_weight = sum(
            JOB_CLUSTERING_WEIGHTS[attribute]
            for attribute in attribute_embeddings
        )

        combined_embedding = np.zeros(
            self.model.get_sentence_embedding_dimension(),
            dtype=np.float32
        )

        for attribute, embedding in attribute_embeddings.items():
            adjusted_weight = (
                JOB_CLUSTERING_WEIGHTS[attribute] / available_weight
            )

            normalized_embedding = np.asarray(
                embedding,
                dtype=np.float32
            )

            norm = np.linalg.norm(normalized_embedding)

            if norm > 0:
                normalized_embedding = normalized_embedding / norm

            combined_embedding += adjusted_weight * normalized_embedding

        combined_norm = np.linalg.norm(combined_embedding)

        if combined_norm == 0:
            raise ValueError(
                "Cannot generate a valid job clustering embedding."
            )

        combined_embedding = combined_embedding / combined_norm

        return combined_embedding.tolist()
    
    def generate_embeddings_batch(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for multiple texts"""
        # Filter out empty texts and replace with placeholder
        processed_texts = []
        for text in texts:
            if text and text.strip():
                processed_texts.append(text)
            else:
                processed_texts.append("empty content")
        
        embeddings = self.model.encode(processed_texts)
        return embeddings.tolist()
    
    def calculate_similarity(self, embedding1: List[float], embedding2: List[float]) -> float:
        """Calculate cosine similarity between two embeddings"""
        embedding1 = np.array(embedding1).reshape(1, -1)
        embedding2 = np.array(embedding2).reshape(1, -1)
        
        similarity = cosine_similarity(embedding1, embedding2)[0][0]
        return float(similarity)
    
    def train_job_clusters(self, job_embeddings: List[List[float]]) -> None:
        """Train K-means clustering on job embeddings"""
        if len(job_embeddings) < settings.NUM_CLUSTERS:
            # If we have fewer jobs than clusters, use the number of jobs
            n_clusters = min(len(job_embeddings), settings.NUM_CLUSTERS)
        else:
            n_clusters = settings.NUM_CLUSTERS
        
        embeddings_array = np.array(job_embeddings)
        
        self.kmeans_model = KMeans(
            n_clusters=n_clusters, 
            random_state=42, 
            n_init=10
        )
        
        cluster_labels = self.kmeans_model.fit_predict(embeddings_array)
        self.cluster_centroids = self.kmeans_model.cluster_centers_
        
        # Save the model
        self._save_clustering_model()
        
        return cluster_labels
    
    def predict_job_cluster(self, job_embedding: List[float]) -> int:
        """Predict which cluster a job belongs to"""
        if self.kmeans_model is None:
            self._load_clustering_model()
        
        if self.kmeans_model is None:
            raise ValueError("K-means model not trained. Please train the model first.")
        
        embedding_array = np.array(job_embedding).reshape(1, -1)
        cluster_id = self.kmeans_model.predict(embedding_array)[0]
        return int(cluster_id)
    
    def get_cluster_centroid(self, cluster_id: int) -> List[float]:
        """Get centroid embedding for a specific cluster"""
        if self.cluster_centroids is None:
            self._load_clustering_model()
        
        if self.cluster_centroids is None or cluster_id >= len(self.cluster_centroids):
            raise ValueError(f"Invalid cluster_id: {cluster_id}")
        
        return self.cluster_centroids[cluster_id].tolist()
    
    def calculate_section_score(self, resume_section_embedding: List[float], 
                              cluster_centroid: List[float]) -> float:
        """Calculate similarity score between resume section and job cluster"""
        similarity = self.calculate_similarity(resume_section_embedding, cluster_centroid)
        # Convert similarity to score (0-100)
        score = max(0, min(100, (similarity + 1) * 50))  # Scale from [-1,1] to [0,100]
        return score
    
    def calculate_weighted_score(self, section_scores: Dict[str, float]) -> float:
        """Calculate final weighted score from individual section scores"""
        weights = {
            'experience': settings.EXPERIENCE_WEIGHT,
            'skills': settings.SKILLS_WEIGHT,
            'education': settings.EDUCATION_WEIGHT,
            'projects': settings.PROJECTS_WEIGHT,
            'certifications': settings.CERTIFICATIONS_WEIGHT
        }
        
        weighted_score = 0.0
        total_weight = 0.0
        
        for section, score in section_scores.items():
            if section in weights and score is not None:
                weighted_score += score * weights[section]
                total_weight += weights[section]
        
        if total_weight > 0:
            final_score = weighted_score / total_weight
        else:
            final_score = 0.0
        
        return min(100, max(0, final_score))
    
    def get_match_type(self, score: float) -> str:
        """Determine match type based on score"""
        if score >= 90:
            return "PERFECT MATCH"
        elif score >= 75:
            return "STRONG MATCH"
        else:
            return "GOOD MATCH"
    
    
    def _save_clustering_model(self):
        """Save the K-means model with its embedding version."""
        model_dir = "models"
        os.makedirs(model_dir, exist_ok=True)

        model_path = os.path.join(
            model_dir,
            "kmeans_job_clusters.pkl"
        )

        with open(model_path, 'wb') as f:
            pickle.dump({
                'embedding_version': JOB_CLUSTERING_EMBEDDING_VERSION,
                'kmeans_model': self.kmeans_model,
                'cluster_centroids': self.cluster_centroids
            }, f)

    def _load_clustering_model(self):
        """Load only a K-means model compatible with current job embeddings."""
        model_path = os.path.join(
            "models",
            "kmeans_job_clusters.pkl"
        )

        if not os.path.exists(model_path):
            raise ValueError(
                "K-means model not found. "
                "Please train the clustering model first."
            )

        with open(model_path, 'rb') as f:
            model_data = pickle.load(f)

        saved_version = model_data.get('embedding_version')

        if saved_version != JOB_CLUSTERING_EMBEDDING_VERSION:
            raise ValueError(
                "Incompatible K-means model version. "
                f"Expected '{JOB_CLUSTERING_EMBEDDING_VERSION}', "
                f"found '{saved_version}'. "
                "Please retrain the clustering model."
            )

        self.kmeans_model = model_data['kmeans_model']
        self.cluster_centroids = model_data['cluster_centroids']

    
    def generate_resume_embeddings(self, parsed_resume: Dict[str, Any]) -> Dict[str, List[float]]:
        """Generate embeddings for different resume sections"""
        embeddings = {}
        
        # Experience embedding
        experience_text = ""
        for exp in parsed_resume.get("experience", []):
            experience_text += f"{exp.get('position', '')} at {exp.get('company', '')}. "
            experience_text += f"{exp.get('description', '')} "
        embeddings['experience'] = self.generate_embedding(experience_text)
        
        # Skills embedding
        skills_data = parsed_resume.get("skills", {})
        skills_text = ""
        for skill_category in skills_data.values():
            if isinstance(skill_category, list):
                skills_text += " ".join(skill_category) + " "
        embeddings['skills'] = self.generate_embedding(skills_text)
        
        # Education embedding
        education_text = ""
        for edu in parsed_resume.get("education", []):
            education_text += f"{edu.get('degree', '')} in {edu.get('field_of_study', '')} "
            education_text += f"from {edu.get('institution', '')}. "
        embeddings['education'] = self.generate_embedding(education_text)
        
        # Projects embedding
        projects_text = ""
        for project in parsed_resume.get("projects", []):
            projects_text += f"{project.get('name', '')}: {project.get('description', '')} "
            projects_text += f"Technologies: {', '.join(project.get('technologies', []))} "
        embeddings['projects'] = self.generate_embedding(projects_text)
        
        # Certifications embedding
        certifications_text = ""
        for cert in parsed_resume.get("certifications", []):
            certifications_text += f"{cert.get('name', '')} from {cert.get('issuer', '')} "
        embeddings['certifications'] = self.generate_embedding(certifications_text)
        
        return embeddings

# Initialize embedding service
embedding_service = EmbeddingService()