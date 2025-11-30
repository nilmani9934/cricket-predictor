import pandas as pd
import random
from datetime import datetime, timedelta

teams = ["India","Australia","England","Pakistan","South Africa","New Zealand","Sri Lanka","Bangladesh","West Indies","Afghanistan"]
venues = ["Delhi","Mumbai","Sydney","Melbourne","Dubai","Auckland","Karachi","Johannesburg","London","Colombo"]

def random_date():
    start = datetime(2016,1,1)
    end = datetime(2024,12,31)
    delta = end - start
    return (start + timedelta(days=random.randint(0, delta.days))).date()

rows = []
for _ in range(500):
    t1, t2 = random.sample(teams, 2)
    venue = random.choice(venues)
    t1_score = random.randint(120, 220)
    t2_score = random.randint(120, 220)
    winner = t1 if t1_score > t2_score else t2

    rows.append({
        "date": random_date(),
        "team1": t1,
        "team2": t2,
        "venue": venue,
        "team1_score": t1_score,
        "team2_score": t2_score,
        "winner": winner
    })

df = pd.DataFrame(rows)
df.to_csv("data/real_matches_dataset.csv", index=False)
print("Dataset created successfully!")
