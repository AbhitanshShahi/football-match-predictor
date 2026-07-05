import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, log_loss, classification_report, confusion_matrix
import joblib

DATA_PATH = "data/processed/final_ml_dataset.csv"

def load_data():
    return pd.read_csv(DATA_PATH)

def prepare_data(df):
    X = df.drop("target", axis=1)
    y = df["target"]

    X = X.fillna(X.median(numeric_only=True))

    return X, y

def build_model():
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("lr", LogisticRegression(max_iter=2000, class_weight="balanced", random_state=42))
    ])
    return model

def evaluate(model, X_test, y_test):
    preds = model.predict(X_test)
    probs = model.predict_proba(X_test)

    print("ACCURACY:", accuracy_score(y_test, preds))
    print("LOG LOSS:", log_loss(y_test, probs))
    print("\nCONFUSION MATRIX:\n", confusion_matrix(y_test, preds))
    print("\nCLASS REPORT:\n", classification_report(y_test, preds))

def save_model(model):
    joblib.dump(model, "ml/models/logistic_regression_model.joblib")

def main():
    df = load_data()

    X, y = prepare_data(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = build_model()
    model.fit(X_train, y_train)

    evaluate(model, X_test, y_test)

    save_model(model)

    print("\nModel saved successfully.")

if __name__ == "__main__":
    main()