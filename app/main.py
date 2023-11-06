from typing import Union, List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from app import models, schemas, crud
from app.database import engine, SessionLocal

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


models.Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/type/{id_type}", response_model=schemas.Type)
def get_type_by_id(id_type: int, db: Session = Depends(get_db)):
    db_type = crud.get_type_by_id(db, id_type)
    if db_type is None:
        raise HTTPException(status_code=404, detail="Type not found")
    return db_type


@app.post("/api/types/", response_model=schemas.Type)
def create_type(type: schemas.TypeCreate, db: Session = Depends(get_db)):
    db_type = crud.get_type_by_name(db, type.name)
    if db_type:
        raise HTTPException(status_code=400, detail='Type already exist')
    return crud.create_type(db=db, type=type)


@app.put("/api/type/{id_type}", response_model=schemas.Type)
def update_type(id_type: int, type: schemas.TypeCreate, db: Session = Depends(get_db)):
    db_type = crud.update_type(db, id_type, type)
    if db_type is None:
        raise HTTPException(status_code=404, detail="Type not found")
    return db_type


@app.post("/db/skill/", response_model=schemas.Skill)
def create_skill(skill: schemas.SkillCreate, db: Session = Depends(get_db)):
    db_skill = crud.create_skill(db, skill)
    if db_skill:
        return db_skill
    raise HTTPException(status_code=404, detail="Skill already exist")


@app.get("/api/skills/", response_model=list[schemas.Skill])
def get_skills(db: Session = Depends(get_db)):
    return crud.get_skills(db)


@app.put("/api/skill/{skill_id}", response_model=schemas.Skill)
def update_skill(skill_id: int, skill: schemas.SkillCreate, db: Session = Depends(get_db)):
    db_skill = crud.update_skill(db, skill_id, skill)
    if db_skill:
        return db_skill
    raise HTTPException(status_code=404, detail="Skill not found")


@app.get("/api/pokemons", response_model=List[schemas.Pokemon])
def get_pokemons(db: Session = Depends(get_db)):
    return crud.get_pokemons(db)


@app.get("/api/pokemon/{pokedex_id}", response_model=schemas.Pokemon)
def get_pokemon_by_id(pokedex_id: int, db: Session = Depends(get_db)):
    db_pokemon = crud.get_pokemon_by_id(db, pokedex_id)
    if db_pokemon:
        return db_pokemon
    raise HTTPException(status_code=404, detail="Pokemon not found")


@app.post("/api/pokemon", response_model=schemas.Pokemon)
def create_pokemon(pokemon: schemas.PokemonCreate, db: Session = Depends(get_db)):
    db_pokemon = crud.create_pokemon(db, pokemon)
    if db_pokemon:
        return db_pokemon
    raise HTTPException(status_code=404, detail="Pokemon already exist")


@app.delete("/api/pokemon/{pokedex_id}", response_model=schemas.Pokemon)
def delete_pokemon(pokedex_id: int, db: Session = Depends(get_db)):
    deleted_pokemon = crud.delete_pokemon_by_id(db, pokedex_id)
    if deleted_pokemon:
        return deleted_pokemon
    raise HTTPException(status_code=404, detail="Pokemon not found")
