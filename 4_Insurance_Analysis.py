import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
import pandas as pd
from db import get_engine

engine = get_engine()

st.title("🛡️ Insurance Analysis")

query = """
SELECT state, SUM(insurance_amount) AS amount
FROM aggregated_insurance
GROUP BY state;
"""

df = pd.read_sql(query, engine)
st.line_chart(df.set_index("state"))
