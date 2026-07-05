import pandas as pd
import numpy as np

TEAMS_PATH = "data/raw/national_teams.csv"
OUTPUT_PATH = "data/processed/teams_clean.csv"

COLUMNS_TO_KEEP = [
    "name",
    "confederation",
    "squad_size",
    "average_age",
    "total_market_value",
    "fifa_ranking"
]

def clean_market_value(value):
    
    if pd.isna(value):
        return np.nan

    value = str(value).replace("€", "").replace(",", "").strip().lower()

    multiplier = 1

    if "b" in value:
        multiplier = 1_000_000_000
        value = value.replace("b", "")
    elif "m" in value:
        multiplier = 1_000_000
        value = value.replace("m", "")

    try:
        return float(value) * multiplier
    except:
        return np.nan

def main():
    df = pd.read_csv(TEAMS_PATH)

    df = df[COLUMNS_TO_KEEP]

    df["total_market_value"] = df["total_market_value"].apply(clean_market_value)

    df["total_market_value"] = df["total_market_value"].fillna(
        df["total_market_value"].median()
    )

    print(df.head())

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumn Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:", df.duplicated().sum())

    print("\nUnique Teams:")
    print(df["name"].nunique())

    print(df["total_market_value"].isna().sum())

    df = df.drop_duplicates()

    df.to_csv(OUTPUT_PATH, index=False)

    print("\nSaved cleaned teams dataset.")


if __name__ == "__main__":
    main()