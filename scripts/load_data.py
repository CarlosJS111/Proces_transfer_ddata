import pandas as pd
import psycopg2

DB_PARAMS = {
    "dbname": "transactions_db",
    "user": "admin",
    "password": "admin",
    "host": "localhost",
    "port": 5432
}

conn = psycopg2.connect(**DB_PARAMS)
cur = conn.cursor()

df = pd.read_csv("data/data_prueba_técnica.csv", dtype=str)

df.columns = df.columns.str.strip()
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
df.dropna(subset=['company_id', 'amount'], inplace=True)

df.rename(columns={'paid_at': 'updated_at'}, inplace=True)

companies = df[['company_id', 'name']].drop_duplicates().dropna().values.tolist()
cur.executemany("INSERT INTO companies (id, name) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING", companies)

charges = df[['id', 'company_id', 'amount', 'status', 'created_at', 'updated_at']].dropna().values.tolist()
cur.executemany("""
    INSERT INTO charges (id, company_id, amount, status, created_at, updated_at) 
    VALUES (%s, %s, %s, %s, %s, %s) 
    ON CONFLICT (id) DO NOTHING
""", charges)

conn.commit()
cur.close()
conn.close()
print("Carga de datos completada.")
