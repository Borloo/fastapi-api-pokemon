from pydantic import BaseModel


class TypeBase(BaseModel):
    name: str


class TypeCreate(TypeBase):
    pass


class Type(TypeBase):
    name: str

    class Config:
        orm_mode = True
