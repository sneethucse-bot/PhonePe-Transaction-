import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

st.title("🗺️ Geographical Insights")

engine = create_engine("sqlite:///phonepe.db")

query = """
SELECT state, SUM(transaction_amount) AS amount
FROM aggregated_transaction
GROUP BY state
"""

df = pd.read_sql(query, engine)

# 🔗 India states GeoJSON
india_geojson = (
    "https://gist.githubusercontent.com/jbrobst/"
    "56c13bbbf9d97d187fea01ca62ea5112/raw/"
    "e388c4cae20aa53cb5090210a42ebb9b765c0a36/"
    "india_states.geojson"
)

fig = px.choropleth(
    df,
    geojson=india_geojson,
    locations="state",
    featureidkey="properties.ST_NM",
    color="amount",
    color_continuous_scale="Blues",
    title="Total Transaction Amount by State"
)

fig.update_geos(
    fitbounds="locations",
    visible=False
)

st.plotly_chart(fig, use_container_width=True)


