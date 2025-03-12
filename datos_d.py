import psycopg2
import pandas as pd

DB_PARAMS = {
    "dbname": "transactions_db",
    "user": "admin",
    "password": "admin",
    "host": "localhost",
    "port": 5432
}

conn = psycopg2.connect(**DB_PARAMS)

query = "SELECT * FROM transactions_summary;"
df = pd.read_sql(query, conn)

print(df)

conn.close()
