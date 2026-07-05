import pandas as pd

MATCHES_PATH = "data/processed/matches_filtered.csv"
ELO_PATH = "data/processed/elo_clean.csv"
TEAMS_PATH = "data/processed/teams_clean.csv"

OUTPUT_PATH = "data/processed/merged_dataset.csv"

def load_data():
    matches = pd.read_csv(MATCHES_PATH)
    elo = pd.read_csv(ELO_PATH)
    teams = pd.read_csv(TEAMS_PATH)
    matches["date"] = pd.to_datetime(matches["date"])
    elo["date"] = pd.to_datetime(elo["date"])
    return matches, elo, teams

def get_latest_elo(elo_df, team, match_date):
    team_history = elo_df[elo_df["team"] == team]
    history = team_history[team_history["date"] <= match_date]
    if history.empty:
        return None
    return history.sort_values("date").iloc[-1]["rating"]

def get_team_info(teams_df, team_name):
    team = teams_df[teams_df["name"] == team_name]

    if team.empty:
        return None

    return team.iloc[0]

def merge_data(matches, elo, teams):

    merged_rows = []

    skipped = 0

    for _, match in matches.iterrows():

        home = match["home_team"]
        away = match["away_team"]
        date = match["date"]

        home_elo = get_latest_elo(elo, home, date)
        away_elo = get_latest_elo(elo, away, date)

        home_team = get_team_info(teams, home)
        away_team = get_team_info(teams, away)

        if (
            home_elo is None
            or away_elo is None
            or home_team is None
            or away_team is None
        ):
            skipped += 1
            continue

        merged_rows.append({

            "date": date,

            "home_team": home,
            "away_team": away,

            "home_score": match["home_score"],
            "away_score": match["away_score"],

            "home_elo": home_elo,
            "away_elo": away_elo,

            "home_fifa_ranking": home_team["fifa_ranking"],
            "away_fifa_ranking": away_team["fifa_ranking"],

            "home_average_age": home_team["average_age"],
            "away_average_age": away_team["average_age"],

            "home_squad_size": home_team["squad_size"],
            "away_squad_size": away_team["squad_size"],

            "home_market_value": home_team["total_market_value"],
            "away_market_value": away_team["total_market_value"],

            "home_confederation": home_team["confederation"],
            "away_confederation": away_team["confederation"],

            "neutral": match["neutral"],
            "tournament": match["tournament"]

        })

    merged = pd.DataFrame(merged_rows)

    print(f"\nMerged Matches : {len(merged)}")
    print(f"Skipped Matches: {skipped}")

    return merged

def main():
    matches, elo, teams = load_data()
    merged = merge_data(matches, elo, teams)
    merged.to_csv(OUTPUT_PATH, index=False)
    print("\nMerged dataset saved successfully.")

if __name__ == "__main__":
    main()