from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base

class Movie(Base):
    
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)


    title = Column(String, index=True)
    summary = Column(String, index=True)

    director_id = Column(Integer, ForeignKey("directors.id"))

    director = relationship("Director", back_populates="movies")