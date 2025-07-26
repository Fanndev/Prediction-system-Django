from fastapi import APIRouter, UploadFile, File
from fastapi import APIRouter, Depends
from app.models.user import User
from app.utils.auth import get_current_active_user

from app.schema.prediction import PredictionResponse
from app.utils import data_processing, visualization
from app.models import prediction_model

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

@router.get("/predictions")
def get_predictions(current_user: User = Depends(get_current_active_user)):
    return {"message": f"Hello {current_user.username}, here are your predictions"}

@router.post("/predictions")
def create_prediction(current_user: User = Depends(get_current_active_user)):
    return {"message": f"Prediction created for user {current_user.username}"}