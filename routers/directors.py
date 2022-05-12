from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..controllers.director import create_director, get_director, get_directors 
from ..controllers.movie import create_movie 

from ..schemas.director import Director, DirectorCreate
from ..schemas.movie import Movie, MovieCreate

router = APIRouter(
    prefix="/directors",
)

@router.post("/", response_model=Director)
def create_user(director: DirectorCreate, db: Session = Depends(get_db)):
    return create_director(db=db, director=director)


@router.get("/", response_model=List[Director])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    directors = get_directors(db=db, skip=skip, limit=limit)
    return directors


@router.get("/{director_id}", response_model=Director)
def read_user(id: int, db: Session = Depends(get_db)):
    director = get_director(db=db, id=id)
    if director is None:
        raise HTTPException(status_code=404, detail="Director not found")
    return director


@router.post("/{director_id}/movies/", response_model=Movie)
def create_item_for_user( director_id: int, movie: MovieCreate, db: Session = Depends(get_db) ):
    return create_movie(db=db, movie=movie, director_id=director_id)
