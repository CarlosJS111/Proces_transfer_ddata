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
query = "SELECT * FROM charges;"
df = pd.read_sql(query, conn)

df.to_parquet("data/extracted_data.parquet", index=False)
conn.close()
print("Extracción completada en formato Parquet.")
