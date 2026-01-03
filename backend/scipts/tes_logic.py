import pickle 
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model_name = 'all-MiniLM-L6-v2' 

def recommend_role(user_query):
    print("Load Data")

    with open('jobs_data.pkl', 'rb') as f:
        df_job  = pickle.load(f)
    
    with open('job_embedding.pkl', 'rb') as f:
        job_embed = pickle.load(f) 
    
    model = SentenceTransformer(model_name) 

    test_cases = [
        # DEVELOPMENT 
        {
            "description": "Persona: Full Stack Dev (High Freq)",
            "query": "I am experienced in building web applications using React, Node.js, MongoDB, and managing both frontend and backend.",
            "expected_keywords": ["full-stack", "developer", "software", "web"]
        },
        {
            "description": "Persona: Blockchain Specialist (Niche)",
            "query": "Interested in smart contracts, Ethereum, Solidity, and distributed ledger technology.",
            "expected_keywords": ["blockchain", "developer", "engineer"]
        },
        {
            "description": "Persona: Mobile Developer",
            "query": "Developing android and ios applications using flutter or swift.",
            "expected_keywords": ["mobile", "app", "developer"]
        },

        # INFRASTRUCTURE & CLOUD 
        {
            "description": "Persona: Cloud & DevOps",
            "query": "Managing AWS infrastructure, CI/CD pipelines, Docker containers, and server automation.",
            "expected_keywords": ["cloud", "devops", "solutions", "architect", "engineer"]
        },
        {
            "description": "Persona: Network Engineer",
            "query": "Configuring routers, switches, LAN/WAN, and troubleshooting network connectivity.",
            "expected_keywords": ["network", "engineer", "administrator"]
        },

        # DATA & AI 
        {
            "description": "Persona: Data Scientist/Analyst",
            "query": "Analyzing big data, creating visualizations, using Python Pandas, and building machine learning models.",
            "expected_keywords": ["data", "scientist", "analyst", "machine learning", "ai"]
        },
        {
            "description": "Persona: AI Ethics (Specific Role)",
            "query": "Ensuring artificial intelligence systems are fair, transparent, and comply with ethical standards.",
            "expected_keywords": ["ethics", "ai", "consultant", "privacy"]
        },

        # SECURITY
        {
            "description": "Persona: Cybersecurity",
            "query": "Protecting systems from cyber attacks, performing vulnerability assessments and penetration testing.",
            "expected_keywords": ["cybersecurity", "security", "analyst", "risk"]
        },

        #  SUPPORT & TRAINING
        {
            "description": "Persona: IT Support (Highest Freq)",
            "query": "Helping users fix computer problems, troubleshooting hardware, and installing software updates.",
            "expected_keywords": ["support", "helpdesk", "specialist", "service desk"]
        },
        {
            "description": "Persona: IT Trainer",
            "query": "Teaching employees how to use new software and conducting technical training sessions.",
            "expected_keywords": ["trainer", "consultant"]
        },

        #  MANAGEMENT & GOVERNANCE
        {
            "description": "Persona: IT Project Manager",
            "query": "Leading project teams, managing timelines, stakeholders, and budget for IT initiatives.",
            "expected_keywords": ["project", "manager", "coordinator"]
        },
        {
            "description": "Persona: IT Procurement/Governance",
            "query": "Managing vendor contracts, purchasing IT assets, and ensuring compliance with regulations.",
            "expected_keywords": ["procurement", "governance", "compliance", "asset", "manager"]
        }
    ] 

    total_tests = len(test_cases)
    passed_test = 0 

    print(f"Running {total_tests} Skenario...\n")
    print('-'*50) 

    for i, case in enumerate(test_cases):
        print(f"Test #{i+1}: {case['description']}")
        print(f" Query: '{case['query'][:60]}'")
        user_vector = model.encode([case["query"]])
        scores = cosine_similarity(user_vector, job_embed)[0] 
        top_indices = np.argsort(scores)[::-1][:5]
        top_5 = []
        visited_role = set()
        cnt = 0 

        for j in top_indices:
            title = df_job.iloc[j]['Job Title']
            clean_title = title.lower().strip() 

            if clean_title not in visited_role:
                top_5.append(title)
                visited_role.add(clean_title)
                cnt+=1 
            if cnt >= 5:
                break 
        
        cek_passed = False 
        hit_keyword = "" 

        all_result = " ".join(top_5).lower()
        for key in case['expected_keywords']:
            if key in all_result:
                cek_passed = True 
                hit_keyword = key 
                break 
        
        if cek_passed:
            print(f"COCOK (Keyword : {hit_keyword})")
            passed_test += 1 
        else:
            print(f"GAGAL (Expected one of : {case['expected_keywords']})") 
        
        print(f"Output : {top_5}")
        print("-"*50) 
    
    success_rate = (passed_test/total_tests)*100
    print(f"Final : {passed_test}/{total_tests} PASS ({success_rate:.1f}%)")


        

if __name__ == "__main__":
    recommend_role("")