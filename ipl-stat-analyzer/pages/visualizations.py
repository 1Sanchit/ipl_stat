import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

matches, deliveries = load_data()

st.title("📈 IPL Visualizations")

chart = st.selectbox(
    "Choose Chart",
    [
        "Top Run Scorers",
        "Most Sixes",
        "Team Wins"
    ]
)

if chart == "Top Run Scorers":

    runs = (
        deliveries.groupby("batter")["batsman_runs"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig = px.bar(
        x=runs.index,
        y=runs.values,
        color=runs.values,
        title="Top 10 Run Scorers"
    )

    st.plotly_chart(fig, use_container_width=True)

elif chart == "Most Sixes":

    sixes = (
        deliveries[deliveries["batsman_runs"] == 6]
        .groupby("batter")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )

    fig = px.bar(
        x=sixes.index,
        y=sixes.values,
        color=sixes.values,
        title="Most Sixes"
    )

    st.plotly_chart(fig, use_container_width=True)

else:

    wins = matches["winner"].value_counts()

    fig = px.pie(
        values=wins.values,
        names=wins.index,
        title="Team Wins"
    )

    st.plotly_chart(fig, use_container_width=True)