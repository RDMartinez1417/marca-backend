from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from app.db import models, schemas

def get_marcas(db: Session, skip: int = 0, limit: int = 100, nombre: str = None, estado: str = None, pais_origen: str = None, clase_niza: int = None, categoria: str = None):
    query= db.query(models.Marca)
    if nombre:
        query = query.filter(models.Marca.nombre.ilike(f"%{nombre}%"))
    if estado:
        query = query.filter(models.Marca.estado == estado)
    if pais_origen:
        query = query.filter(models.Marca.pais_origen.ilike(f"%{pais_origen}%"))
    if clase_niza:
        query = query.filter(models.Marca.clase_niza == clase_niza)
    if categoria:
        query = query.filter(models.Marca.categoria.ilike(f"%{categoria}%"))
    return query.offset(skip).limit(limit).all()

def get_marca(db: Session, marca_id: int):
    return db.query(models.Marca).filter(models.Marca.id == marca_id).first()

def create_marca(db: Session, marca: schemas.MarcaCreate):
    db_marca = models.Marca(
        nombre=marca.nombre,
        descripcion=marca.descripcion,
        estado=marca.estado,
        pais_origen=marca.pais_origen,
        clase_niza=marca.clase_niza,
        categoria=marca.categoria,
        numero_registro=marca.numero_registro,
        fecha_registro=marca.fecha_registro,
        usuario_creacion=marca.usuario_creacion,
        usuario_actualizacion=marca.usuario_actualizacion,
        sitio_web=marca.sitio_web,
        titular=marca.titular,
        monitoreo_falsificacion=marca.monitoreo_falsificacion
    )
    try:
        db.add(db_marca)
        db.commit()
        db.refresh(db_marca)
        return db_marca
    except IntegrityError:
        db.rollback()
        return None

def update_marca(db: Session, marca_id: int, marca: schemas.MarcaUpdate):
    db_marca = db.query(models.Marca).filter(models.Marca.id == marca_id).first()
    if db_marca:
        db_marca.nombre = marca.nombre
        db_marca.descripcion = marca.descripcion
        db_marca.estado = marca.estado
        db_marca.pais_origen = marca.pais_origen
        db_marca.clase_niza = marca.clase_niza
        db_marca.categoria = marca.categoria
        db_marca.numero_registro = marca.numero_registro
        db_marca.fecha_registro = marca.fecha_registro
        db_marca.usuario_creacion = marca.usuario_creacion
        db_marca.usuario_actualizacion = marca.usuario_actualizacion
        db_marca.sitio_web = marca.sitio_web
        db_marca.titular = marca.titular
        db_marca.monitoreo_falsificacion = marca.monitoreo_falsificacion
        try:
            db.commit()
            db.refresh(db_marca)
            return db_marca
        except IntegrityError:
            db.rollback()
            raise
    return None

def delete_marca(db: Session, marca_id: int):
    db_marca = db.query(models.Marca).filter(models.Marca.id == marca_id).first()
    if db_marca:
        db.delete(db_marca)
        db.commit()
    return db_marca
def get_total_marcas(db: Session):
    return db.query(models.Marca).count()
def get_marca_summary(db: Session):
    counts = db.query(
        models.Marca.estado, 
        func.count(models.Marca.estado)
    ).group_by(
        models.Marca.estado
    ).all()
    result = {estado: count for estado, count in counts}
    return result
def get_categories(db: Session):
    return db.query(models.Marca.categoria).distinct().all()
