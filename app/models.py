from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

from app.database import Base


class Type(Base):
    __tablename__ = "type"

    name = Column(String, unique=True, index=True, primary_key=True)
