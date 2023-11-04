from typing import Union

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

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
