from sqlalchemy.orm import Session

import app.models as models
import app.schemas as schemas


def get_type(db: Session, type: str):
    return db.query(models.Type).filter(models.Type.name == type).first()


def get_types(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Type).offset(skip).limit(limit).all()


def create_type(db: Session, type: schemas.TypeCreate):
    db_type = models.Type(name=type.name)
    db.add(db_type)
    db.commit()
    db.refresh(db_type)
    return db_type
