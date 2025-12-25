import streamlit as st
import pandas as pd
from db import get_engine

engine = get_engine()

st.title("🏆 Top Performers")

query = """
SELECT state, SUM(transaction_amount) AS amount
FROM aggregated_transaction
GROUP BY state
ORDER BY amount DESC
LIMIT 10;
"""

df = pd.read_sql(query, engine)
st.dataframe(df)
