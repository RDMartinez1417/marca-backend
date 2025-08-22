from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import models, database
from app.api import routes

# Crear tablas
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="CRUD Marcas - FastAPI + SQLite/PostgreSQL")

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes especificar dominios en vez de "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(routes.router)
