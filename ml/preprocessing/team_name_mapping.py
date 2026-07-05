import pandas as pd

MATCH_PATH = "data/processed/matches_clean.csv"
ELO_PATH = "data/processed/elo_clean.csv"
TEAMS_PATH = "data/processed/teams_clean.csv"


def normalize(name):
    return str(name).replace("\xa0", " ").strip()

def load_data():
    matches = pd.read_csv(MATCH_PATH)
    elo = pd.read_csv(ELO_PATH)
    teams = pd.read_csv(TEAMS_PATH)

    return matches, elo, teams

def clean_names(matches, elo, teams):
    matches["home_team"] = matches["home_team"].apply(normalize)
    matches["away_team"] = matches["away_team"].apply(normalize)

    elo["team"] = elo["team"].apply(normalize)

    teams["name"] = teams["name"].apply(normalize)

    return matches, elo, teams

def get_valid_teams(elo, teams):
    elo_teams = set(elo["team"].unique())
    fifa_teams = set(teams["name"].unique())

    valid = elo_teams.intersection(fifa_teams)

    return valid

def filter_matches(matches, valid_teams):
    filtered = matches[
        (matches["home_team"].isin(valid_teams)) &
        (matches["away_team"].isin(valid_teams))
    ].copy()

    return filtered

def main():
    matches, elo, teams = load_data()

    matches, elo, teams = clean_names(matches, elo, teams)

    valid_teams = get_valid_teams(elo, teams)

    filtered_matches = filter_matches(matches, valid_teams)

    print("\nOriginal matches:", len(matches))
    print("Filtered matches:", len(filtered_matches))
    print("Valid teams:", len(valid_teams))

    filtered_matches.to_csv(
        "data/processed/matches_filtered.csv",
        index=False
    )

    print("\nSaved filtered dataset.")


if __name__ == "__main__":
    main()

