import streamlit as st
import pandas as pd
from src.predict import predict_match

st.title("Cricket Match Predictor")

players = pd.read_csv("data/player_stats.csv")
venues  = pd.read_csv("data/venue_stats.csv")

team1 = st.selectbox("Select Team 1", players.team.unique())
team2 = st.selectbox("Select Team 2", players.team.unique())
venue = st.selectbox("Select Venue", venues.venue.unique())

if st.button("Predict"):
    t1 = players[players.team==team1]
    t2 = players[players.team==team2]

    t1_bat = t1.career_runs.mean()
    t1_bowl = t1.career_wkts.mean()
    t2_bat = t2.career_runs.mean()
    t2_bowl = t2.career_wkts.mean()

    v = venues[venues.venue==venue].iloc[0]

    result = predict_match(t1_bat,t1_bowl,t2_bat,t2_bowl,v.batting_bias,v.home_adv)
    st.success(result)
