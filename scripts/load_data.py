import pandas as pd
import psycopg2
from psycopg2 import sql

DB_PARAMS = {
    "dbname": "transactions_db",
    "user": "admin",
    "password": "admin",
    "host": "localhost",
    "port": 5432
}

# Conectar a la BD
conn = psycopg2.connect(**DB_PARAMS)
cur = conn.cursor()

# Crear esquema
cur.execute("""
    CREATE TABLE IF NOT EXISTS companies (
        id VARCHAR(50) PRIMARY KEY,
        name VARCHAR(130) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS charges (
        id VARCHAR(50) PRIMARY KEY,
        company_id VARCHAR(50) NOT NULL,
        amount DECIMAL(16,2) NOT NULL,
        status VARCHAR(30) NOT NULL,
        created_at TIMESTAMP NOT NULL,
        updated_at TIMESTAMP NULL,
        FOREIGN KEY (company_id) REFERENCES companies(id)
    );
""")

# Leer CSV y limpiar datos
df = pd.read_csv("data/data_prueba_técnica.csv")
df['updated_at'] = None

# Insertar datos en 'companies' evitando duplicados
companies = df[['company_id', 'name']].drop_duplicates().dropna().values.tolist()
cur.executemany("INSERT INTO companies (id, name) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING", companies)

# Insertar datos en 'charges'
charges = df[['id', 'company_id', 'amount', 'status', 'created_at', 'updated_at']].dropna().values.tolist()
cur.executemany("INSERT INTO charges (id, company_id, amount, status, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)", charges)

conn.commit()
cur.close()
conn.close()
print("Carga de datos completada.")
