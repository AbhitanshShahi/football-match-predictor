import axios from "axios";
import type { PredictionRequest, PredictionResponse } from "./types";

const BASE_URL = import.meta.env.VITE_BACKEND_URL;

export async function predictMatch(
  payload: PredictionRequest,
): Promise<PredictionResponse> {
  try {
    const response = await axios.post<PredictionResponse>(
      `${BASE_URL}/predict`,
      payload,
    );

    return response.data;
  } catch (error) {
    throw new Error("Prediction API failed");
  }
}
