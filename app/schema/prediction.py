from pydantic import BaseModel

class PredictionResponse(BaseModel):
    dates: list[str]
    predictions: list[float]
    plot_base64: str