from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Type(Base):
    __tablename__ = "Type"

    id = Column(Integer, unique=True, index=True, primary_key=True)
    name = Column(String, unique=True, index=True)
    skills = relationship("Skill", back_populates="type")


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


class Pokemon(Base):
    __tablename__ = "Pokemon"

    pokedex_number = Column(Integer, unique=True, primary_key=True)
    name = Column(String, unique=True)
    height = Column(Integer)
    weight = Column(Integer)
    basic_stats = Column(Integer)
    image = Column(String, unique=True)
    # type_s = relationship("Type", back_populates="types")
    # skill_s = relationship("Skill", back_populates="skills")
