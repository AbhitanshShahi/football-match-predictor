from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from ml.inference.predictor import load_model, predict_match
from ml.inference.feature_builder import load_data, build_team_lookup

@asynccontextmanager
async def lifespan(app: FastAPI):

    global model, team_lookup

    df = load_data()
    team_lookup = build_team_lookup(df)
    model = load_model()

    print("Model loaded successfully")
    yield 
    print("Shutting down")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class MatchRequest(BaseModel):
    home_team: str
    away_team: str
    tournament: str = "FIFA World Cup"
    neutral: int = 0

model = None
team_lookup = None


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(match: MatchRequest):

    result = predict_match(
        model=model,
        team_lookup=team_lookup,
        home_team=match.home_team,
        away_team=match.away_team,
        tournament=match.tournament,
        neutral=match.neutral
    )

    return {
        "input": match.model_dump(),
        "prediction": result
    }