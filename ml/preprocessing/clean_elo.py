import pandas as pd

ELO_PATH = "data/raw/eloratings.csv"
OUTPUT_PATH = "data/processed/elo_clean.csv"


def main():
    df = pd.read_csv(ELO_PATH)

    print("\n========== ELO DATASET ==========")
    print(df.head())

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumn Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:", df.duplicated().sum())

    df["date"] = pd.to_datetime(df["date"], format="mixed")

    df = df.drop_duplicates()

    print("\nDate Range:")
    print(df["date"].min(), "->", df["date"].max())

    print("\nUnique Teams:")
    print(df["team"].nunique())

    df.to_csv(OUTPUT_PATH, index=False)

    print("\nSaved cleaned Elo dataset.")


if __name__ == "__main__":
    main()