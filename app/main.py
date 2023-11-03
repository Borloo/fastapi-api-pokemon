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


@app.post("/type/", response_model=schemas.Type)
def createType(type: schemas.TypeCreate, db: Session = Depends(get_db)):
    db_type = crud.get_type(db, type.name)
    if db_type:
        raise HTTPException(status_code=400, detail='Type already exist')
    return crud.create_type(db=db, type=type)


@app.get("/types/", response_model=list[schemas.Type])
def getTypes(skip: int = 0, limit: int = 0, db: Session = Depends(get_db)):
    types = crud.get_types(db, skip=skip, limit=limit)
    return types
