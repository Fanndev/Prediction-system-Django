from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    # JWT Settings
    SECRET_KEY: str = "your-secret-key-change-in-production-make-it-very-long-and-random"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database
    DATABASE_URL: str = "sqlite:///./db/app.db"
    
    # App Settings
    APP_NAME: str = "CSV Prediction API"
    DEBUG: bool = True
    
    class Config:
        env_file = ".env"

settings = Settings()
class Settings(BaseSettings):
    
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    DATABASE_URL: str = "sqlite:///./db/app.db"
    
    APP_NAME: str = "CSV Prediction API"
    DEBUG: bool = True
    
    class Config:
        env_file = ".env"

settings = Settings()