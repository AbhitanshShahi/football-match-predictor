import pandas as pd

MATCHES_PATH = "data/raw/match_results_raw.csv"
OUTPUT_PATH = "data/processed/matches_clean.csv"


def main():
    df = pd.read_csv(MATCHES_PATH)

    print("\n========== MATCH DATASET ==========")
    print(df.head())

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumn Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:", df.duplicated().sum())

    df["date"] = pd.to_datetime(df["date"])

    df = df.drop_duplicates()

    print("\nDate Range:")
    print(df["date"].min(), "->", df["date"].max())

    print("\nUnique Teams:")
    teams = sorted(
        set(df["home_team"]).union(set(df["away_team"]))
    )
    print(len(teams))

    df.to_csv(OUTPUT_PATH, index=False)

    print("\nSaved cleaned matches dataset.")


if __name__ == "__main__":
    main()