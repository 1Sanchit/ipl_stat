import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

matches, deliveries = load_data()

st.title("📊 Dashboard")

c1, c2, c3 = st.columns(3)

c1.metric("Matches", len(matches))
c2.metric("Teams", matches["team1"].nunique())
c3.metric("Players", deliveries["batter"].nunique())

st.markdown("---")

top_runs = (
    deliveries.groupby("batter")["batsman_runs"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig = px.bar(
    x=top_runs.index,
    y=top_runs.values,
    color=top_runs.values,
    labels={"x": "Player", "y": "Runs"},
    title="Top 10 Run Scorers"
)

st.plotly_chart(fig, use_container_width=True)