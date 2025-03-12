import psycopg2

DB_PARAMS = {
    "dbname": "transactions_db",
    "user": "admin",
    "password": "admin",
    "host": "localhost",
    "port": 5432
}

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    
    cur.execute("""
        CREATE OR REPLACE VIEW daily_transactions AS
        SELECT 
            DATE(created_at) AS transaction_date,
            company_id,
            SUM(amount) AS total_amount
        FROM charges
        GROUP BY transaction_date, company_id;
    """)
    
    conn.commit()
    print("Vista 'daily_transactions' creada exitosamente.")
    
    cur.close()
    conn.close()
except Exception as e:
    print("Error:", e)
