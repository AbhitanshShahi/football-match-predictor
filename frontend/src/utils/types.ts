export type PredictionRequest = {
  home_team: string;
  away_team: string;
  tournament?: string;
  neutral?: number;
};

export type PredictionOutput = {
  home_win: number;
  draw: number;
  away_win: number;
};

export type PredictionResponse = {
  input: PredictionRequest;
  prediction: PredictionOutput;
};