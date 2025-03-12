import sqlite3
import pandas as pd
import pytest

@pytest.fixture
def setup_database():
    """Crea una base de datos en memoria con datos de prueba."""
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    # Crear tabla
    cur.execute("""
        CREATE TABLE charges (
            id INTEGER PRIMARY KEY, 
            company_id TEXT, 
            amount REAL, 
            status TEXT, 
            created_at TEXT, 
            updated_at TEXT
        )
    """)

    # Insertar datos de prueba
    test_data = [
        (1, "A123", 1000.50, "paid", "2024-03-01", "2024-03-01"),
        (2, "A123", 2000.75, "paid", "2024-03-01", "2024-03-01"),
        (3, "B456", 500.25, "paid", "2024-03-02", "2024-03-02"),
        (4, "A123", 1500.00, "paid", "2024-03-02", "2024-03-02"),
    ]
    cur.executemany("INSERT INTO charges VALUES (?, ?, ?, ?, ?, ?)", test_data)
    conn.commit()
    yield conn  # Pasar la conexión a las pruebas
    conn.close()

def test_transaction_summary(setup_database):
    """Verifica que el total por día y compañía sea el esperado."""
    conn = setup_database

    df = pd.read_sql_query("""
        SELECT DATE(updated_at) AS transaction_date, company_id, SUM(amount) AS total_amount
        FROM charges 
        GROUP BY transaction_date, company_id
        ORDER BY transaction_date, company_id
    """, conn)

    expected_data = [
        {"transaction_date": "2024-03-01", "company_id": "A123", "total_amount": 3001.25},
        {"transaction_date": "2024-03-02", "company_id": "A123", "total_amount": 1500.00},
        {"transaction_date": "2024-03-02", "company_id": "B456", "total_amount": 500.25},
    ]

    expected_df = pd.DataFrame(expected_data)

        pd.testing.assert_frame_equal(df, expected_df, check_dtype=False, check_exact=False, atol=0.01)
