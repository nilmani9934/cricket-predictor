import pandas as pd
from xgboost import XGBClassifier
import pickle

df = pd.read_csv("data/match_features_enhanced.csv")

X = df[["team1_bat","team1_bowl","team2_bat","team2_bowl","batting_bias","home_adv"]]
y = df["winner"]

model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
model.fit(X, y)

with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully!")
