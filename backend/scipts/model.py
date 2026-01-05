import os 
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import pandas as pd 
import re 
import pickle 
from sentence_transformers import SentenceTransformer 

Dataset = '../../dataset/Job_New.csv'
model_name = 'all-MiniLM-L6-v2' 

def clean_text(text):
    if not isinstance(text, str):
        return ""
    
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'[^a-zA-Z0-9\s.,]', '', text)
    text = text.lower().strip()
    return text 

def main():
    print("Loading Dataset")
    try:
        df = pd.read_csv(Dataset)
        print(f"Dataset : {len(df)} baris.")
    except Exception as e:
        print(f"Gagal: {e}")
        return 
    

    print("Kolom tersedia: ", df.columns.tolist())
    col_title = 'Job Title'
    col_desc = 'Job Description' 
    col_skills = 'Required Skills'

    df['combined_text'] = (df[col_title].apply(clean_text) + " " + df[col_desc].apply(clean_text) + " " + df[col_skills].apply(clean_text) + " " + df[col_skills].apply(clean_text))
    model = SentenceTransformer(model_name)
    print("Embedding Process")
    job_embeddings = model.encode(df['combined_text'].tolist(), show_progress_bar=True) 
    print("Save File")
    fe_data = df[[col_title, col_desc, col_skills]].copy()
    with open('jobs_data.pkl','wb') as f:
        pickle.dump(fe_data,f)
    
    with open('job_embedding.pkl', 'wb') as f:
        pickle.dump(job_embeddings,f) 
    
    print("Done")

if __name__ == "__main__":
    main()

