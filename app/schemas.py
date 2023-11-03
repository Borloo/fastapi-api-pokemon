from pydantic import BaseModel


class TypeBase(BaseModel):
    id: int
    name: str


class TypeCreate(TypeBase):
    pass


class Type(TypeBase):
    id: int

    class Config:
        orm_mode = True