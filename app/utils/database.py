from app.config.database import Base, engine
from app.models.user import User  

def create_tables():
    Base.metadata.create_all(bind=engine)

def init_db():
    create_tables()
    print("Database initialized successfully!")