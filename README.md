# ⚽ Football Match Predictor

> A full-stack ML system that predicts international football match outcomes using team strength modeling and probabilistic classification.

## 🔗 Live Links

* Frontend: *https://football-match-predictor-ivory.vercel.app/*
* Backend API: *https://football-match-predictor-fge5.onrender.com/*
* Model (Hugging Face): *https://huggingface.co/abhitanshshahi/football-match-predictor-xgboost/resolve/main/xgboost_model.joblib*

---

## 📌 What This Project Does

This system predicts the probability of a football match result between two national teams:

* 🟢 Home Win
* 🟡 Draw
* 🔴 Away Win

Instead of relying on raw match statistics, the model learns from **relative team strength differentials** such as Elo ratings, FIFA rankings, and squad metrics.

---

## 🧠 Key Idea (Important)

Football outcomes are not absolute—they are comparative.

So the model is trained on:

> **(Home Team Features − Away Team Features)**

This makes predictions more stable across tournaments and eras.

---

## 🏗️ System Design

```
User Input (React UI)
        ↓
FastAPI Backend
        ↓
Feature Engineering Layer
        ↓
XGBoost Model (Hugging Face)
        ↓
Probability Output
        ↓
Frontend Visualization
```

---

## 📊 Input Features

### Team Strength Signals

* FIFA Ranking
* Elo Rating
* Squad Size
* Average Age
* Market Value

### Match Context

* Tournament Type
* Neutral Venue Flag

### Engineered Features

* Elo Difference
* Ranking Difference
* Squad Depth Difference
* Market Value Difference
* Age Gap
* Tournament Encoding

---

## 🤖 Machine Learning Model

* Algorithm: **XGBoost Classifier**
* Task: Multi-class probabilistic classification
* Output: calibrated probabilities for:
  * Home Win
  * Draw
  * Away Win

The model was selected after benchmarking against Logistic Regression and Random Forest, with XGBoost giving the best performance.

---

## 🧰 Tech Stack

### Machine Learning
Python, Pandas, NumPy, Scikit-learn, XGBoost, Joblib

### Backend
FastAPI, Uvicorn

### Frontend
React, TypeScript, Tailwind CSS

### Deployment
* Frontend: Vercel
* Backend: Render
* Model Hosting: Hugging Face

---

## 📡 API Reference

### Health Check

```
GET /health
```

Response:

```json
{ "status": "ok" }
```

### Predict Match Outcome

```
POST /predict
```

Request:

```json
{
  "home_team": "Spain",
  "away_team": "Germany",
  "tournament": "FIFA World Cup",
  "neutral": 0
}
```

Response:

```json
{
  "prediction": {
    "home_win": 0.54,
    "draw": 0.23,
    "away_win": 0.23
  }
}
```

---

## 📁 Repository Structure

```
football-match-predictor/
├── backend/
├── frontend/
├── ml/
│   ├── training/
│   ├── inference/
│   ├── preprocessing/
│   ├── feature_engineering/
│   └── models/
├── data/
├── requirements.txt
└── README.md
```

---

## 🚀 Local Setup

```bash
git clone https://github.com/your-username/football-match-predictor.git
cd football-match-predictor
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

Then open:

```
http://127.0.0.1:8000/docs
```

---

## 🤖 Model Hosting

The trained model is hosted on **Hugging Face Hub** and loaded dynamically at backend startup for inference.

---

## 📈 Why XGBoost?

XGBoost was chosen because:

* Handles structured tabular data effectively
* Captures non-linear feature interactions
* Performs well on small-to-medium datasets
* Produces well-calibrated probabilities (important for sports prediction)

---

## 🔮 Future Improvements

* Player-level feature integration
* Time-decayed team form
* Injury/suspension modeling
* Betting odds fusion
* Tournament simulation engine
* Explainability layer (SHAP values)
* Probability calibration improvements

---

## ⚠️ Disclaimer

This project is for educational and research purposes only.
Match outcomes are inherently uncertain and should not be treated as guarantees.

---

## 🧾 License

MIT License
