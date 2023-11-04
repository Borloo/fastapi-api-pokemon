from sqlalchemy.orm import Session

import app.models as models
import app.schemas as schemas


def get_type_by_id(db: Session, id_type: int):
    return db.query(models.Type).filter(models.Type.id == id_type).first()


def get_type_by_name(db: Session, name_type: str):
    return db.query(models.Type).filter(models.Type.name == name_type).first()


def get_types(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Type).offset(skip).limit(limit).all()


def get_skill_by_name(db: Session, name_skill: str):
    return db.query(models.Skill).filter(models.Skill.name == name_skill).first()


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


def create_skill(db: Session, skill: schemas.SkillCreate):
    db_skill = get_skill_by_name(db, skill.name)
    if db_skill:
        return None
    db_skil = models.Skill(**skill.model_dump())
    db.add(db_skil)
    db.commit()
    db.refresh(db_skil)
    return db_skil
