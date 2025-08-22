import os
from dotenv import load_dotenv

# Cargar archivo .env
load_dotenv()

class Settings:
    PROJECT_NAME: str = "CRUD Marcas - FastAPI"
    ENV: str = os.getenv("ENV", "development")
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()
