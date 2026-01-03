import pandas as pd 
dataset = 'dataset/Job.xlsx'
col_title = 'Job Title' 

def roles():
    try:
        df = pd.read_excel(dataset)
    except Exception as e:
        print(f"Error:{e}")
        return 
    
    df['clean_title'] = df[col_title].astype(str).str.lower().str.strip()

    cnt_role = df['clean_title'].value_counts()
    unique_value = len(cnt_role) 

    print(f"Total data: {len(df)}")
    print(f"Total Role: {unique_value}")

    with open('role_report.txt', 'w', encoding='utf-8') as f:
        f.write("Daftar Role")
        for role in cnt_role.items():
            f.write(f"{role}\n")

if __name__ == "__main__":
    roles()