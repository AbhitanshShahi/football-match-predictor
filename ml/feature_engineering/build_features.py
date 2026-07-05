import pandas as pd

PATH = "data/processed/merged_dataset.csv"

def load_data():
    return pd.read_csv(PATH)

def create_features(df):
    df["elo_diff"] = df["home_elo"] - df["away_elo"]
    df["rank_diff"] = df["home_fifa_ranking"] - df["away_fifa_ranking"]
    df["age_diff"] = df["home_average_age"] - df["away_average_age"]
    df["squad_size_diff"] = df["home_squad_size"] - df["away_squad_size"]
    df["market_value_diff"] = df["home_market_value"] - df["away_market_value"]
    df["is_neutral"] = df["neutral"].astype(int)
    return df

def create_target(df):
    df["target"] = df.apply(
        lambda row: 0 if row["home_score"] > row["away_score"]
        else 2 if row["home_score"] < row["away_score"]
        else 1,
        axis=1
    )
    return df

def encode_tournament(df):
    df = pd.get_dummies(df, columns=["tournament"], drop_first=True)
    return df

def select_features(df):
    drop_cols = [
        "home_team",
        "away_team",
        "home_score",
        "away_score",
        "date",
        "home_elo",
        "away_elo",
        "home_fifa_ranking",
        "away_fifa_ranking",
        "home_average_age",
        "away_average_age",
        "home_squad_size",
        "away_squad_size",
        "home_market_value",
        "away_market_value",
        "neutral",
        "home_confederation", 
        "away_confederation"
    ]
    df = df.drop(columns=drop_cols)
    return df

def main():
    df = load_data()

    df = create_features(df)
    df = create_target(df)
    df = encode_tournament(df)
    df = select_features(df)

    df.to_csv("data/processed/final_ml_dataset.csv", index=False)

    print("Final dataset shape:", df.shape)
    print("Saved final_ml_dataset.csv")

if __name__ == "__main__":
    main()