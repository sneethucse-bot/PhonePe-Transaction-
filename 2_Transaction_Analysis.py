import streamlit as st
import pandas as pd
from db import get_engine

engine = get_engine()

st.title("📊 Transaction Analysis")

year = st.selectbox("Select Year", [2018, 2019, 2020, 2021, 2022])

query = f"""
SELECT transaction_type, SUM(transaction_amount) AS amount
FROM aggregated_transaction
WHERE year = {year}
GROUP BY transaction_type;
"""

df = pd.read_sql(query, engine)

st.bar_chart(df.set_index("transaction_type"))
