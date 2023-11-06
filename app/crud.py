from typing import List

from sqlalchemy.orm import Session

import app.models as models
import app.schemas as schemas


def get_type_by_id(db: Session, id_type: int):
    return db.query(models.Type).filter(models.Type.id == id_type).first()


def get_type_by_name(db: Session, name_type: str):
    return db.query(models.Type).filter(models.Type.name == name_type).first()


def get_types(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Type).offset(skip).limit(limit).all()


def get_types_by_pokemon(db: Session, pokemon_types: List[int]):
    return db.query(models.Type).filter(models.Type.id.in_(pokemon_types)).all()


def get_skills(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Skill).offset(skip).limit(limit).all()


def get_skill_by_name(db: Session, name_skill: str):
    return db.query(models.Skill).filter(models.Skill.name == name_skill).first()


def get_skill_by_id(db: Session, skill_id: int):
    return db.query(models.Skill).filter(models.Skill.id == skill_id).first()


def get_skills_by_pokemon(db: Session, pokemon_skills: List[int]):
    return db.query(models.Skill).filter(models.Skill.id.in_(pokemon_skills)).all()


def get_pokemons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pokemon).offset(skip).limit(limit).all()


def get_pokemon_by_id(db: Session, pokedex_id: int):
    return db.query(models.Pokemon).filter(models.Pokemon.pokedex_id == pokedex_id).first()


def get_pokemon_by_name(db: Session, pokemon_name: str):
    return db.query(models.Pokemon).filter(models.Pokemon.name == pokemon_name).first()


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


def create_pokemon(db: Session, pokemon: schemas.PokemonCreate):
    db_pokemon_name = get_pokemon_by_name(db, pokemon.name)
    db_pokemon_id = get_pokemon_by_id(db, pokemon.pokedex_id)
    db_types = get_types_by_pokemon(db, pokemon.types)
    db_skills = get_skills_by_pokemon(db, pokemon.skills)
    if db_pokemon_name or db_pokemon_id or not db_types or not db_skills:
        return None
    db_pokemon: schemas.PokemonCreate = models.Pokemon(**pokemon.model_dump(exclude={"types", "skills"}))
    db_pokemon.types = db_types
    db_pokemon.skills = db_skills
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon


def delete_pokemon_by_id(db: Session, pokedex_id: int):
    db_pokemon = get_pokemon_by_id(db, pokedex_id)
    if db_pokemon:
        db.delete(db_pokemon)
        db.commit()
        return db_pokemon
    return None


def update_pokemon_by_id(db: Session, pokedex_id: int, pokemon: schemas.PokemonCreate):
    db_pokemon = get_pokemon_by_id(db, pokedex_id)
    db_types = get_types_by_pokemon(db, pokemon.types)
    db_skills = get_skills_by_pokemon(db, pokemon.skills)
    if db_pokemon or not db_types or not db_skills:
        db_pokemon.name = pokemon.name
        db_pokemon.size = pokemon.size
        db_pokemon.weight = pokemon.weight
        db_pokemon.basic_stats = pokemon.basic_stats
        db_pokemon.image = pokemon.image
        db_pokemon.types = db_types
        db_pokemon.skills = db_skills
        db.commit()
        db.refresh(db_pokemon)
        return db_pokemon
    return None
