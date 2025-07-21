import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "CSV Upload Time Series Predictor"
    VERSION = "1.0.0"
    MODEL_PATH = "saved_model/model.h5"

settings = Settings()