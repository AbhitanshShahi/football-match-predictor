import pandas as pd
import joblib
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score, log_loss, confusion_matrix, classification_report

DATA_PATH = "data/processed/final_ml_dataset.csv"

def load_data():
    return pd.read_csv(DATA_PATH)

def prepare_data(df):
    X = df.drop("target", axis=1)
    y = df["target"]

    X = X.fillna(X.median(numeric_only=True))

    return X, y

def build_model():
    base_model = XGBClassifier(
        objective="multi:softprob",
        num_class=3,
        random_state=42,
        eval_metric="mlogloss"
    )

    params = {
        "n_estimators": [200, 300],
        "learning_rate": [0.05, 0.1],
        "max_depth": [5, 7],
        "min_child_weight": [1, 3]
    }

    grid = GridSearchCV(
        estimator=base_model,
        param_grid=params,
        scoring="neg_log_loss",
        cv=5,
        n_jobs=-1,
        verbose=2
    )

    return grid

def evaluate(model, X_test, y_test):
    preds = model.predict(X_test)
    probs = model.predict_proba(X_test)

    print("ACCURACY:", accuracy_score(y_test, preds))
    print("LOG LOSS:", log_loss(y_test, probs))
    print("\nCONFUSION MATRIX:\n", confusion_matrix(y_test, preds))
    print("\nCLASS REPORT:\n", classification_report(y_test, preds))

def show_feature_importance(model, X):
    importance = pd.DataFrame({
        "Feature": X.columns,
        "Importance": model.feature_importances_
    })

    importance = importance.sort_values(by="Importance", ascending=False)

    print("\nTOP 20 FEATURES:\n")
    print(importance.head(20))

def save_model(model):
    joblib.dump(model, "ml/models/xgboost_model.joblib")

def main():
    df = load_data()

    X, y = prepare_data(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    grid = build_model()

    print("\nTraining GridSearchCV...\n")
    grid.fit(X_train, y_train)

    print("\nBEST PARAMETERS:")
    print(grid.best_params_)

    print("\nBEST CV LOG LOSS:")
    print(-grid.best_score_)

    best_model = grid.best_estimator_

    evaluate(best_model, X_test, y_test)

    show_feature_importance(best_model, X)

    save_model(best_model)

    print("\nModel saved successfully.")

if __name__ == "__main__":
    main()