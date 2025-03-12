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

df = pd.read_parquet("data/transformed_data.parquet")
charges = df[['id', 'company_id', 'amount', 'status', 'created_at', 'updated_at']].values.tolist()
cur.executemany("INSERT INTO charges (id, company_id, amount, status, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING", charges)

conn.commit()
cur.close()
conn.close()
print("Datos dispersados en la base de datos.")
