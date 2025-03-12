import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB_PARAMS = {
    "dbname": os.getenv("POSTGRES_DB"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "host": os.getenv("POSTGRES_HOST"),
    "port": os.getenv("POSTGRES_PORT")
}

df_charges = pd.read_csv("charges_transformed.csv")

conn = psycopg2.connect(**DB_PARAMS)
cur = conn.cursor()

companies = df_charges[['company_id', 'company_name']].drop_duplicates().values.tolist()
cur.executemany("INSERT INTO companies (id, name) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING", companies)

charges = df_charges[['id', 'company_id', 'amount', 'status', 'created_at', 'updated_at']].values.tolist()
cur.executemany("INSERT INTO charges VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING", charges)

conn.commit()
cur.close()
conn.close()
print("Datos insertados correctamente.")
