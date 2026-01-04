import pickle
import numpy as np
import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
artifacts_dir = os.path.join(base_dir, "artifacts")

class CareerRecommender:
    def __init__(self):
        self.df_jobs = None
        self.job_embeddings = None
        self.model = None
        self._load_artifacts()

    def _load_artifacts(self):
        try:
            with open(os.path.join(artifacts_dir, "jobs_data.pkl"), "rb") as f:
                self.df_jobs = pickle.load(f)
            
            with open(os.path.join(artifacts_dir, "job_embedding.pkl"), "rb") as f:
                self.job_embeddings = pickle.load(f)
            
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
            
        except FileNotFoundError:
            print("Artifacts Not Found")

    def get_recommendations(self, user_tags: list[str], top_k=5):
        query = " ".join(user_tags)
        user_vector = self.model.encode([query])
        scores = cosine_similarity(user_vector, self.job_embeddings)[0]
        top_indices = np.argsort(scores)[::-1]
        
        recommendations = []
        seen_roles = set()
        
        for idx in top_indices:
            title = self.df_jobs.iloc[idx]['Job Title']
            clean_title = title.lower().strip()
            
            if clean_title not in seen_roles:
                recommendations.append({
                    "title": title,
                    "match_score": float(scores[idx]), 
                    "description": str(self.df_jobs.iloc[idx]['Job Description'])
                })
                seen_roles.add(clean_title)
            
            if len(recommendations) >= top_k:
                break
                
        return recommendations
    
recommender_engine = CareerRecommender()