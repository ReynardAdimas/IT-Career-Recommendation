# 🚀 Nuntun: IT Career Recommender

**Nuntun** is an intelligent web application designed to help users discover suitable IT career paths. By taking an interactive personality and technical preference quiz, users receive personalized job recommendations powered by a Natural Language Processing (NLP) recommendation engine.

---

## ✨ Key Features

- **Interactive Career Quiz**  
  A dynamic questionnaire that maps user preferences (e.g., visual aesthetics vs. logic, teamwork vs. solo work) to technical tags.

- **AI-Powered Recommendations**  
  Uses ML-based text embeddings to calculate similarity between user interests and real-world IT job data.

- **Job Insights**  
  Displays job titles, descriptions, and match scores.

---

## 🛠 Tech Stack

### Backend & AI
- **Python** – Core programming language  
- **FastAPI** – API framework  
- **Sentence Transformers** (`all-MiniLM-L6-v2`) – Text embeddings  
- **Scikit-learn** – Cosine similarity computation  
- **Pandas** – Data manipulation  

### Frontend
- **React (Vite)** – Frontend framework  
- **TailwindCSS** – Utility-first CSS  
- **Radix UI** – Accessible UI primitives  
- **Framer Motion** – Animations  
- **Axios** – API integration  

---

## 📂 Project Structure

```bash
nuntun/
├── backend/
│   ├── app/
│   │   ├── services/
│   │   │   └── recommender.py  # Inference engine logic
│   │   └── main.py             # FastAPI entry point
│   ├── artifacts/              # Generated PKL files (embeddings & data)
│   ├── data/
│   │   └── questions.json      # Quiz questions database
│   ├── scripts/
│   │   ├── model.py            # Script to train/embed job data
│   │   └── tes_logic.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.jsx
│   ├── package.json
│   └── tailwind.config.js
├── dataset/
│   └── Job_New.csv             # Raw dataset
└── notebook/
    └── EDA.ipynb               # Exploratory Data Analysis
``` 

## 🧠 How the Machine Learning Works 
Nuntun uses a Content-Based Filtering approach with Semantic Search: 
1. Preprocessing: The raw dataset is processed. The Job Title, Job Description, and Required Skills are cleaned and combined into a single text block for each job. 
2. Embedding Generation: The script `backend/scripts/model.py` uses the `sentence-transformers/all-MiniLM-L6-v2` model to convert the combined text of every job into a dense vector (embedding). These are saved in `job_embedding.pkl`. 
3. User Profiling: When a user takes the quiz, their answer collect spesific tags (e.g., "frontend","logic","creative"). 
4. Inference: 
    - The backend combines the user tags into a query string. 
    - This query is encoded into a vector using the same model. 
    - Cosine Similiarity is calculated between the user vector and all job vector. 
    - The system returns the top 5 jobs with the highest similiarity scores. 

## 🔌 API Documentation 
1. **Health Check**
    - Endpoint: `GET / ` 
    - Response: 
    ```json 
    {
        "status":"active", 
        "message":"Welcome to Nuntun: IT Career Recommendation"
    } 
    ```
2. **Get Quiz Questions** :
Retrieves the list of questions for the frontend application.
    - Endpoint: `POST /api/recommend` 
    - Body: 
    ```json
    {
        "tags": ["frontend", "creative", "ui designer", "visual"]
    }
    ``` 
    - Response: 
    ```json 
    [
        {
            "title": "UI/UX Designer",
            "match_score": 0.85,
            "description": "Designing user interfaces..."
        },
        ...
    ] 
    ``` 

## 🤝 Contribution 
Contributions are welcome! Please follow these steps: 
1. Fork the repository 
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the brach (`git push origin feature/YourFeature`)
5. Open a pull Request 
---
*Reynard Adimas N, 2026*