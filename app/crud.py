from sqlalchemy.orm import Session

import app.models as models
import app.schemas as schemas


def get_type_by_id(db: Session, id_type: int):
    return db.query(models.Type).filter(models.Type.id == id_type).first()


def get_type_by_name(db: Session, name_type: str):
    return db.query(models.Type).filter(models.Type.name == name_type).first()


def get_types(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Type).offset(skip).limit(limit).all()


def create_type(db: Session, type: schemas.TypeCreate):
    db_type = models.Type(name=type.name)
    db.add(db_type)
    db.commit()
    db.refresh(db_type)
    return db_type


def update_type(db: Session, type_id: int, type: schemas.TypeCreate):
    db_type = get_type_by_id(db, type_id)
    if db_type:
        db_type.name = type.name
        db.commit()
        db.refresh(db_type)
        return db_type
    return None
