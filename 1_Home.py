import streamlit as st
import pandas as pd
from db import get_engine
from queries import HOME_KPI_QUERY, STATE_WISE_QUERY

engine = get_engine()

st.title("🏠 Home Overview")

kpi_df = pd.read_sql(HOME_KPI_QUERY, engine)

col1, col2 = st.columns(2)
col1.metric("💰 Total Transaction Amount", f"₹{kpi_df.total_amount[0]:,.0f}")
col2.metric("🔁 Total Transactions", f"{kpi_df.total_count[0]:,.0f}")

state_df = pd.read_sql(STATE_WISE_QUERY, engine)
st.bar_chart(state_df.set_index("state"))
