from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from app.db import models, database
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.api import routes

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="CRUD Marcas")

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    for error in errors:
        if "fecha_registro" in error["loc"]:
            return JSONResponse(
                status_code=422,
                content={"detail": "La fecha de registro ingresada no es válida. Por favor, usa el formato 'YYYY-MM-DD'."},
            )
            
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)
