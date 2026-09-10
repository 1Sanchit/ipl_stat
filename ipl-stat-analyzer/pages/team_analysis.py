import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

matches, deliveries = load_data()

st.title("🏆 Team Analysis")

teams = sorted(matches["team1"].unique())

team = st.selectbox("Select Team", teams)

played = matches[
    (matches["team1"] == team) |
    (matches["team2"] == team)
]

wins = len(matches[matches["winner"] == team])

losses = len(played) - wins

c1, c2, c3 = st.columns(3)

c1.metric("Matches", len(played))
c2.metric("Wins", wins)
c3.metric("Losses", losses)

fig = px.pie(
    values=[wins, losses],
    names=["Wins", "Losses"],
    title="Win Percentage"
)

st.plotly_chart(fig)