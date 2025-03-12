CREATE TABLE IF NOT EXISTS companies (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(130) NOT NULL
);

CREATE TABLE IF NOT EXISTS charges (
    id VARCHAR(50) PRIMARY KEY,
    company_id VARCHAR(50) NOT NULL,
    amount NUMERIC(16,2) NOT NULL DEFAULT 0.00,
    status VARCHAR(30) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    paid_at TIMESTAMP NULL,
    FOREIGN KEY (company_id) REFERENCES companies(id)

CREATE OR REPLACE VIEW total_transactions_per_day AS
SELECT
    DATE(created_at) AS transaction_date,
    c.name AS company_name,
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_amount
FROM charges ch
JOIN companies c ON ch.company_id = c.id
WHERE ch.status = 'paid'
GROUP BY DATE(created_at), c.name;

);
