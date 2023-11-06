from pydantic import BaseModel
from typing import List


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


class PokemonBase(BaseModel):
    pokedex_id: int
    name: str
    size: float
    weight: float
    basic_stats: float
    image: str
    types: List[int]
    skills: List[int]


class PokemonCreate(PokemonBase):
    pass


class Pokemon(PokemonBase):
    types: List[Type] = []
    skills: List[Skill] = []

    class Config:
        orm_mode = True
