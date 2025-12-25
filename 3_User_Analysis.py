import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from db import get_engine

st.header("👥 User Analysis")

engine = get_engine()

# Filters
years = pd.read_sql("SELECT DISTINCT year FROM aggregated_user ORDER BY year", engine)["year"]
year = st.selectbox("Select Year", years)

query = f"""
SELECT
    state,
    SUM(registered_users) AS users,
    SUM(app_opens) AS app_opens
FROM aggregated_user
WHERE year = {year}
GROUP BY state
ORDER BY users DESC
"""

df = pd.read_sql(query, engine)

# Display
st.dataframe(df)

st.subheader("Top States by Registered Users")
top10 = df.head(10)

fig, ax = plt.subplots()
ax.pie(
    top10["users"],
    labels=top10["state"],
    autopct="%1.1f%%",
    startangle=90
)
ax.axis("equal")

st.pyplot(fig)
