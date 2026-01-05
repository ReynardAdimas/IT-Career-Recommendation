import json
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.services.recommender import recommender_engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Nuntun: IT Career Recommender API") 

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"]
)
class UserAnswer(BaseModel):
    tags: List[str] 

class JobRecommendation(BaseModel):
    title: str
    match_score: float
    description: str


@app.get("/")
def read_root():
    return {"status": "active", "message": "Welcome to Nuntun: IT Career Recommender API"}

@app.get("/api/questions")
def get_questions():
    json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "questions.json")
    try:
        with open(json_path, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Questions file not found")

@app.post("/api/recommend", response_model=List[JobRecommendation])
def predict_career(payload: UserAnswer):
    if not payload.tags:
        raise HTTPException(status_code=400, detail="No tags provided")
    
    results = recommender_engine.get_recommendations(payload.tags)
    return results