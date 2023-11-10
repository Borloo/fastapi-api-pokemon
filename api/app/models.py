from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Float, Table
from sqlalchemy.orm import relationship

from app.database import Base


pokemons_types = Table(
    "pokemons_types",
    Base.metadata,
    Column("pokemon_id", Integer, ForeignKey("Pokemon.pokedex_id"), primary_key=True),
    Column("type_id", Integer, ForeignKey("Type.id"), primary_key=True)
)


pokemons_skills = Table(
    "pokemons_skills",
    Base.metadata,
    Column("pokemon_id", Integer, ForeignKey("Pokemon.pokedex_id"), primary_key=True),
    Column("skill_id", Integer, ForeignKey("Skill.id"), primary_key=True)
)


class Type(Base):
    __tablename__ = "Type"

    id = Column(Integer, unique=True, index=True, primary_key=True)
    name = Column(String, unique=True, index=True)
    skills = relationship("Skill", back_populates="type")
    pokemons = relationship("Pokemon", secondary=pokemons_types, back_populates="types")


class Skill(Base):
    __tablename__ = "Skill"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text)
    power = Column(Integer)
    accurency = Column(Integer)
    life_max = Column(Integer)
    type_name = Column(String, ForeignKey("Type.name"))

    type = relationship("Type", back_populates="skills")
    pokemons = relationship("Pokemon", secondary=pokemons_skills, back_populates="skills")


class Pokemon(Base):
    __tablename__ = "Pokemon"

    pokedex_id = Column(Integer, unique=True, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    size = Column(Float)
    weight = Column(Float)
    basic_stats = Column(Integer)
    image = Column(Text, unique=True)

    types = relationship("Type", secondary=pokemons_types, back_populates="pokemons")
    skills = relationship("Skill", secondary=pokemons_skills, back_populates="pokemons")
