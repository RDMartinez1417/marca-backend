from sqlalchemy.orm import Session
from app.db import models, schemas

def get_marcas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Marca).offset(skip).limit(limit).all()

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
        numero_Registro=marca.numero_Registro,
        fecha_registro=marca.fecha_registro,
        usuario_creacion=marca.usuario_creacion,
        usuario_actualizacion=marca.usuario_actualizacion,
        sitio_web=marca.sitio_web,
        titular=marca.titular,
        monitoreo_falsificacion=marca.monitoreo_falsificacion
    )
    db.add(db_marca)
    db.commit()
    db.refresh(db_marca)
    return db_marca

def update_marca(db: Session, marca_id: int, marca: schemas.MarcaUpdate):
    db_marca = db.query(models.Marca).filter(models.Marca.id == marca_id).first()
    if db_marca:
        db_marca.nombre = marca.nombre
        db_marca.descripcion = marca.descripcion
        db_marca.estado = marca.estado
        db_marca.pais_origen = marca.pais_origen
        db.clase_niza = marca.clase_niza
        db_marca.categoria = marca.categoria
        db_marca.numero_Registro = marca.numero_Registro
        db_marca.fecha_registro = marca.fecha_registro
        db_marca.usuario_creacion = marca.usuario_creacion
        db_marca.usuario_actualizacion = marca.usuario_actualizacion
        db_marca.sitio_web = marca.sitio_web
        db_marca.titular = marca.titular
        db_marca.monitoreo_falsificacion = marca.monitoreo_falsificacion
        db.commit()
        db.refresh(db_marca)
    return db_marca

def delete_marca(db: Session, marca_id: int):
    db_marca = db.query(models.Marca).filter(models.Marca.id == marca_id).first()
    if db_marca:
        db.delete(db_marca)
        db.commit()
    return db_marca
