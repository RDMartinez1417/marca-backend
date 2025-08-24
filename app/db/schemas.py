from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional,List

class MarcaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    estado: Optional[str] = None
    pais_origen: Optional[str] = None
    clase_niza: Optional[int] = None
    categoria: Optional[str] = None
    numero_registro: Optional[str] = None
    fecha_registro: Optional[date] = None
    usuario_creacion: Optional[str] = None
    usuario_actualizacion: Optional[str] = None
    sitio_web: Optional[str] = None
    titular: Optional[str] = None
    monitoreo_falsificacion: Optional[bool] = False

class MarcaCreate(MarcaBase):
    pass

class MarcaUpdate(MarcaBase):
    pass

class Marca(MarcaBase):
    id: int
    fecha_creacion: datetime
    fecha_actualizacion: Optional[datetime] = None

    class Config:
        orm_mode = True
class MarcaPaginatedResponse(BaseModel):
    marcas: List[Marca]
    total_count: int
