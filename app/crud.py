from sqlalchemy.orm import Session

import app.models as models
import app.schemas as schemas


def get_type_by_id(db: Session, id_type: int):
    return db.query(models.Type).filter(models.Type.id == id_type).first()


def get_type_by_name(db: Session, name_type: str):
    return db.query(models.Type).filter(models.Type.name == name_type).first()


def get_types(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Type).offset(skip).limit(limit).all()


def get_skills(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Skill).offset(skip).limit(limit).all()


def get_pokemons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pokemon).offset(skip).limit(limit).all()


def get_skill_by_name(db: Session, name_skill: str):
    return db.query(models.Skill).filter(models.Skill.name == name_skill).first()


def get_skill_by_id(db: Session, skill_id: int):
    return db.query(models.Skill).filter(models.Skill.id == skill_id).first()


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


def update_skill(db: Session, skill_id: int, skill: schemas.SkillCreate):
    db_skill = get_skill_by_id(db, skill_id)
    if db_skill:
        db_skill.name = skill.name
        db_skill.description = skill.description
        db_skill.power = skill.power
        db_skill.accurency = skill.accurency
        db_skill.life_max = skill.life_max
        db_skill.type_name = skill.type_name
        db.commit()
        db.refresh(db_skill)
        return db_skill
    return None
