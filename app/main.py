from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
from app.utils.database import init_db
from app.api.auth import router as auth_router
from app.api.routes import router as api_router

init_db()

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "CSV Prediction API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}