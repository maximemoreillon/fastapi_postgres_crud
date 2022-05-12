from sqlalchemy.orm import Session

from ..models import director as model
from ..schemas import director as schema

def get_director(db: Session, id: int):
    return db.query(model.Director).filter(model.Director.id == id).first()

def get_directors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Director).offset(skip).limit(limit).all()

def create_director(db: Session, director: schema.DirectorCreate):
    new_director = model.Director(name=director.name)
    db.add(new_director)
    db.commit()
    db.refresh(new_director)
    return new_director