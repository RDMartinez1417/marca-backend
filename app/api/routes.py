from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db import crud, schemas
from app.utils.dependencies import get_db

router = APIRouter(prefix="/marcas", tags=["marcas"])

@router.get("/", response_model=List[schemas.Marca])
def read_marcas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_marcas(db, skip=skip, limit=limit)

@router.get("/{marca_id}", response_model=schemas.Marca)
def read_marca(marca_id: int, db: Session = Depends(get_db)):
    db_marca = crud.get_marca(db, marca_id=marca_id)
    if db_marca is None:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return db_marca

@router.post("/", response_model=schemas.Marca)
def create_marca(marca: schemas.MarcaCreate, db: Session = Depends(get_db)):
    return crud.create_marca(db=db, marca=marca)

@router.put("/{marca_id}", response_model=schemas.Marca)
def update_marca(marca_id: int, marca: schemas.MarcaUpdate, db: Session = Depends(get_db)):
    db_marca = crud.update_marca(db=db, marca_id=marca_id, marca=marca)
    if db_marca is None:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return db_marca

@router.delete("/{marca_id}")
def delete_marca(marca_id: int, db: Session = Depends(get_db)):
    db_marca = crud.delete_marca(db=db, marca_id=marca_id)
    if db_marca is None:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return {"detail": "Marca eliminada"}
