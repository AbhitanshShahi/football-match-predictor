import pandas as pd

DATA_PATH = "data/processed/merged_dataset.csv"


def load_data():
    df = pd.read_csv(DATA_PATH)
    return df


def build_team_lookup(df):

    home_cols = [
        "home_team", "home_elo", "home_fifa_ranking",
        "home_average_age", "home_squad_size", "home_market_value"
    ]

    away_cols = [
        "away_team", "away_elo", "away_fifa_ranking",
        "away_average_age", "away_squad_size", "away_market_value"
    ]

    home_df = df[home_cols].rename(columns={
        "home_team": "team",
        "home_elo": "elo",
        "home_fifa_ranking": "rank",
        "home_average_age": "age",
        "home_squad_size": "squad_size",
        "home_market_value": "market_value"
    })

    away_df = df[away_cols].rename(columns={
        "away_team": "team",
        "away_elo": "elo",
        "away_fifa_ranking": "rank",
        "away_average_age": "age",
        "away_squad_size": "squad_size",
        "away_market_value": "market_value"
    })

    combined = pd.concat([home_df, away_df])
    grouped = combined.groupby("team").mean()

    team_lookup = {}

    for team, row in grouped.iterrows():
        team_lookup[team] = row.to_dict()

    return team_lookup


def get_team(team_lookup, team):

    if team not in team_lookup:
        raise ValueError(f"Team not found: {team}")

    return team_lookup[team]


def build_features(team_lookup, home_team, away_team, tournament="FIFA World Cup", neutral=0):

    home = get_team(team_lookup, home_team)
    away = get_team(team_lookup, away_team)

    features = {}

    features["elo_diff"] = home["elo"] - away["elo"]
    features["rank_diff"] = home["rank"] - away["rank"]
    features["age_diff"] = home["age"] - away["age"]
    features["squad_size_diff"] = home["squad_size"] - away["squad_size"]
    features["market_value_diff"] = home["market_value"] - away["market_value"]
    features["is_neutral"] = int(neutral)

    features[f"tournament_{tournament}"] = 1

    return pd.DataFrame([features])


def main():

    df = load_data()
    team_lookup = build_team_lookup(df)

    sample = build_features(
        team_lookup,
        "Spain",
        "Germany",
        "FIFA World Cup",
        0
    )

    print(sample)


if __name__ == "__main__":
    main()