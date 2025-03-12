import psycopg2
import time

DB_PARAMS = {
    "dbname": "transactions_db",
    "user": "admin",
    "password": "admin",
    "host": "localhost",
    "port": 5432
}


def test_db_connection(retries=5, delay=3):
    """ Intenta conectarse a la base de datos con reintentos en caso de fallo. """
    for i in range(retries):
        try:
            conn = psycopg2.connect(**DB_PARAMS)
            cur = conn.cursor()
            cur.execute("SELECT 1;")
            result = cur.fetchone()
            assert result == (1,)
            print("Conexión a la base de datos exitosa")
            cur.close()
            conn.close()
            return
        except Exception as e:
            print(f"Intento {i+1}/{retries}: Error en la conexión a la BD: {e}")
            time.sleep(delay)

    assert False, "No se pudo conectar a la base de datos después de varios intentos"

test_db_connection()
