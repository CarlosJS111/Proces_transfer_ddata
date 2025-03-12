DROP VIEW IF EXISTS transactions_summary;
CREATE VIEW transactions_summary AS
SELECT 
    DATE(updated_at) AS transaction_date,
    company_id,
    SUM(amount) AS total_amount
FROM charges
WHERE updated_at IS NOT NULL
GROUP BY transaction_date, company_id
ORDER BY transaction_date, company_id;
