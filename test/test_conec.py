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
    
    cur.execute("SELECT version();")
    print("Conexión exitosa a:", cur.fetchone()[0])

    cur.close()
    conn.close()
except Exception as e:
    print("Error al conectar:", e)
