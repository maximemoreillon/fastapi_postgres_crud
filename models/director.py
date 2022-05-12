from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class Director(Base):
    __tablename__ = "director"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, unique=True, index=True)
    age = Column(Integer)

    movies = relationship("Movie", back_populates="director")