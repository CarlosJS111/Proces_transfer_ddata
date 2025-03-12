import pandas as pd
import psycopg2

DB_PARAMS = {
    "dbname": "transactions_db",
    "user": "admin",
    "password": "admin",
    "host": "localhost",
    "port": 5432
}

# Conectar a la base de datos
conn = psycopg2.connect(**DB_PARAMS)
cur = conn.cursor()

# Leer CSV y limpiar datos
df = pd.read_csv("data/data_prueba_técnica.csv", dtype=str)

# Eliminar espacios en blanco en los nombres de las columnas y datos
df.columns = df.columns.str.strip()
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Convertir `amount` a número y eliminar filas sin `company_id`
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
df.dropna(subset=['company_id', 'amount'], inplace=True)

# Renombrar `paid_at` a `updated_at`
df.rename(columns={'paid_at': 'updated_at'}, inplace=True)

# Insertar en 'companies' evitando duplicados
companies = df[['company_id', 'name']].drop_duplicates().dropna().values.tolist()
cur.executemany("INSERT INTO companies (id, name) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING", companies)

# Insertar datos en 'charges'
charges = df[['id', 'company_id', 'amount', 'status', 'created_at', 'updated_at']].dropna().values.tolist()
cur.executemany("""
    INSERT INTO charges (id, company_id, amount, status, created_at, updated_at) 
    VALUES (%s, %s, %s, %s, %s, %s) 
    ON CONFLICT (id) DO NOTHING
""", charges)

# Guardar cambios y cerrar conexión
conn.commit()
cur.close()
conn.close()
print("Carga de datos completada.")
