import streamlit as st
from utils.data_loader import load_data

matches, deliveries = load_data()

st.title("🏆 IPL Records")

# Top Run Scorer
top_run = (
    deliveries.groupby("batter")["batsman_runs"]
    .sum()
    .sort_values(ascending=False)
)

st.subheader("🏏 Top Run Scorer")
st.write(f"**{top_run.index[0]}** - {top_run.iloc[0]} Runs")

# Most Sixes
most_sixes = (
    deliveries[deliveries["batsman_runs"] == 6]
    .groupby("batter")
    .size()
    .sort_values(ascending=False)
)

st.subheader("💥 Most Sixes")
st.write(f"**{most_sixes.index[0]}** - {most_sixes.iloc[0]} Sixes")

# Most Fours
most_fours = (
    deliveries[deliveries["batsman_runs"] == 4]
    .groupby("batter")
    .size()
    .sort_values(ascending=False)
)

st.subheader("🏏 Most Fours")
st.write(f"**{most_fours.index[0]}** - {most_fours.iloc[0]} Fours")