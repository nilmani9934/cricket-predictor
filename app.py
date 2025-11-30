import streamlit as st
from src.predict import predict_match

st.title("Cricket Predictor")

team1 = st.text_input("Team 1")
team2 = st.text_input("Team 2")

if st.button("Predict"):
    st.success(predict_match(team1,team2))
