import pandas as pd
import joblib
import requests
from io import BytesIO

from ml.inference.feature_builder import load_data, build_team_lookup, build_features

MODEL_URL = "https://huggingface.co/abhitanshshahi/football-match-predictor-xgboost/resolve/main/xgboost_model.joblib"


def load_model():
    response = requests.get(MODEL_URL)

    if response.status_code != 200:
        raise Exception("Failed to download model from Hugging Face")

    return joblib.load(BytesIO(response.content))


def get_feature_columns(model):
    return model.get_booster().feature_names


def align_features(df, feature_columns):

    aligned = pd.DataFrame(0, index=df.index, columns=feature_columns)

    for col in df.columns:
        if col in aligned.columns:
            aligned[col] = df[col]

    return aligned


def predict_match(model, team_lookup, home_team, away_team,
                  tournament="FIFA World Cup", neutral=0):

    features_df = build_features(
        team_lookup,
        home_team,
        away_team,
        tournament,
        neutral
    )

    feature_columns = get_feature_columns(model)
    features_df = align_features(features_df, feature_columns)

    probs = model.predict_proba(features_df)[0]

    return {
        "home_win": float(probs[0]),
        "draw": float(probs[1]),
        "away_win": float(probs[2])
    }