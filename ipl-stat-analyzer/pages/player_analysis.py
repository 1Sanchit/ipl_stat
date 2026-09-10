import streamlit as st
import plotly.express as px

from utils.data_loader import load_deliveries


deliveries = load_deliveries()


st.title("👤 Player Analysis")


players = sorted(
    deliveries["batter"].unique()
)


player = st.selectbox(
    "Select Player",
    players
)


player_data = deliveries[
    deliveries["batter"] == player
]


runs = player_data[
    "batsman_runs"
].sum()


balls = len(player_data)


six = len(
    player_data[
        player_data["batsman_runs"] == 6
    ]
)


four = len(
    player_data[
        player_data["batsman_runs"] == 4
    ]
)


strike_rate = round(
    runs/balls*100,
    2
)


col1,col2,col3,col4 = st.columns(4)


col1.metric(
    "Runs",
    runs
)

col2.metric(
    "Strike Rate",
    strike_rate
)

col3.metric(
    "Sixes",
    six
)

col4.metric(
    "Fours",
    four
)



chart = (
player_data
.groupby("match_id")
["batsman_runs"]
.sum()
.reset_index()
)


fig = px.line(
    chart,
    x="match_id",
    y="batsman_runs",
    markers=True,
    title=f"{player} Performance"
)


st.plotly_chart(
    fig,
    use_container_width=True
)