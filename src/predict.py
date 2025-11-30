import pandas as pd
import pickle

def predict_match(t1_bat, t1_bowl, t2_bat, t2_bowl, bias, home):
    with open("models/model.pkl","rb") as f:
        model = pickle.load(f)
    X = pd.DataFrame([{
        "team1_bat":t1_bat, "team1_bowl":t1_bowl,
        "team2_bat":t2_bat, "team2_bowl":t2_bowl,
        "batting_bias":bias, "home_adv":home
    }])
    pred = model.predict(X)[0]
    return "Team 1 Wins" if pred==1 else "Team 2 Wins"
