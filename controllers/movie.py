from sqlalchemy.orm import Session

from ..models import movie as model
from ..schemas import movie as schema

def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Movie).offset(skip).limit(limit).all()

def get_movie(db: Session, id: int):
    return db.query(model.Movie).filter(model.Movie.id == id).first()

def create_movie(db: Session, movie: schema.MovieCreate, director_id: int):
    new_movie = model.Movie(**movie.dict(), director_id=director_id)
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie