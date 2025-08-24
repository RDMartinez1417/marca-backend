from sqlalchemy import Column, Integer, String, DateTime, Enum, Date, Boolean
from datetime import datetime
from app.db.database import Base
import enum

class EstadoMarca(str, enum.Enum):
    activo = "Activo"
    inactivo = "Inactivo"
    pendiente = "Pendiente"

class Marca(Base):
    __tablename__ = "marcas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True, nullable=False)
    descripcion = Column(String, nullable=True)
    estado = Column(Enum(EstadoMarca), default=EstadoMarca.activo, nullable=False,index=True)
    pais_origen = Column(String, nullable=True,index=True)
    clase_niza = Column(Integer, nullable=True,index=True)
    categoria = Column(String, nullable=True,index=True)
    numero_registro = Column(String, nullable=True)
    fecha_registro = Column(Date, nullable=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, onupdate=datetime.utcnow, nullable=True)
    usuario_creacion = Column(String, nullable=True)
    usuario_actualizacion = Column(String, nullable=True)
    sitio_web = Column(String, nullable=True)
    titular = Column(String, nullable=False)
    monitoreo_falsificacion = Column(Boolean, default=False)