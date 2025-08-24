from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError,OperationalError,DataError,SQLAlchemyError 
from typing import List,Optional,Dict

from app.db import crud, schemas
from app.utils.dependencies import get_db

router = APIRouter(prefix="/marcas", tags=["marcas"])

@router.get("/list", response_model=schemas.MarcaPaginatedResponse)
def read_marcas(skip: int = 0, limit: int = 100,nombre: Optional[str] = None,
    estado: Optional[str] = None,
    pais_origen: Optional[str] = None,
    clase_niza: Optional[int] = None,
    categoria: Optional[str] = None, db: Session = Depends(get_db)):
    marcas=crud.get_marcas(db, skip=skip, limit=limit, nombre=nombre, estado=estado, pais_origen=pais_origen, clase_niza=clase_niza, categoria=categoria)
    total_count = db.query(crud.models.Marca).count()
    return {"marcas": marcas, "total_count": total_count}


@router.get("/list/{marca_id}", response_model=schemas.Marca)
def read_marca(marca_id: int, db: Session = Depends(get_db)):
    db_marca = crud.get_marca(db, marca_id=marca_id)
    if db_marca is None:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return db_marca

@router.post("/create", response_model=schemas.Marca)
def create_marca(marca: schemas.MarcaCreate, db: Session = Depends(get_db)):
    try:
        db_marca =crud.create_marca(db=db, marca=marca)
        if not db_marca:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Ya existe una marca con ese nombre."
            )
        return db_marca
    except DataError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Uno o más valores proporcionados no son válidos. Por favor, revisa el tipo de dato."
        )
    except OperationalError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="El servicio de la base de datos no está disponible. Por favor, inténtalo de nuevo más tarde."
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error inesperado de base de datos: {e}"
        )

@router.put("/update/{marca_id}", response_model=schemas.Marca)
def update_marca(marca_id: int, marca: schemas.MarcaUpdate, db: Session = Depends(get_db)):
    try:
        db_marca = crud.update_marca(db=db, marca_id=marca_id, marca=marca)
        if db_marca is None:
            raise HTTPException(status_code=404, detail="Marca no encontrada")
        return db_marca
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya existe otra marca con ese nombre."
        )
    except DataError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Uno o más valores proporcionados no son válidos. Por favor, revisa el tipo de dato."
        )
    except OperationalError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="El servicio de la base de datos no está disponible. Por favor, inténtalo de nuevo más tarde."
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error inesperado de base de datos: {e}"
        )

@router.delete("/delete/{marca_id}")
def delete_marca(marca_id: int, db: Session = Depends(get_db)):
    db_marca = crud.delete_marca(db=db, marca_id=marca_id)
    if db_marca is None:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return {"detail": "Marca eliminada"}

@router.get("/summary", response_model=Dict[str, int])
def read_marca_summary(db: Session = Depends(get_db)):
    counts = crud.get_marca_summary(db=db)
    return counts

@router.get("/categories", response_model=List[str])
def get_unique_categories(db: Session = Depends(get_db)):
    categories_tuples = crud.get_categories(db=db)
    print( categories_tuples)
    categories = [c[0] for c in categories_tuples if c[0] is not None]
    return categories