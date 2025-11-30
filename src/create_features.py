import pandas as pd

matches = pd.read_csv("data/real_matches_dataset.csv")
players = pd.read_csv("data/player_stats.csv")
venues  = pd.read_csv("data/venue_stats.csv")

def team_strength(team):
    df = players[players.team == team]
    return df["career_runs"].mean(), df["career_wkts"].mean()

rows = []
for _, r in matches.iterrows():
    t1 = r.team1
    t2 = r.team2

    t1_runs, t1_wkts = team_strength(t1)
    t2_runs, t2_wkts = team_strength(t2)

    v = venues[venues.venue == r.venue].iloc[0]

    rows.append({
        "team1_bat": t1_runs,
        "team1_bowl": t1_wkts,
        "team2_bat": t2_runs,
        "team2_bowl": t2_wkts,
        "batting_bias": v.batting_bias,
        "home_adv": v.home_adv,
        "winner": 1 if r.winner == r.team1 else 0
    })

df_feat = pd.DataFrame(rows)
df_feat.to_csv("data/match_features_enhanced.csv", index=False)
print("Features created successfully!")
