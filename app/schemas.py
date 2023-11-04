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


class SkillBase(BaseModel):
    name: str
    description: str
    power: int
    accurency: int
    life_max: int
    type_name: str


class SkillCreate(SkillBase):
    pass


class Skill(SkillBase):
    id: int

    class Config:
        orm_mode = True
