from fastapi import APIRouter, UploadFile, File
from schema.prediction import PredictionResponse
from utils import data_processing, visualization
from models import prediction_model

import pandas as pd
import io

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict_from_csv(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    
    processed_df = data_processing.preprocess_dataframe(df)
    model, scaler = prediction_model.train_model(processed_df)
    future_dates, predictions = prediction_model.predict_future(processed_df, model, scaler)
    
    plot_base64 = visualization.plot_predictions(processed_df, future_dates, predictions)

    return PredictionResponse(
        dates=[d.strftime("%Y-%m-%d") for d in future_dates],
        predictions=[float(p) for p in predictions],
        plot_base64=plot_base64
    )