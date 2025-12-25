HOME_KPI_QUERY = """
SELECT 
    SUM(transaction_amount) AS total_amount,
    SUM(transaction_count) AS total_count
FROM aggregated_transaction;
"""

STATE_WISE_QUERY = """
SELECT state, SUM(transaction_amount) AS amount
FROM aggregated_transaction
GROUP BY state;
"""
TOP_STATES_QUERY = """
SELECT state, SUM(transaction_amount) AS amount
FROM aggregated_transaction
GROUP BY state
ORDER BY amount DESC
LIMIT 10;
"""