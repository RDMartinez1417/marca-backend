from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import models, database
from app.api import routes

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="CRUD Marcas")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)
