from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session

from ..main import get_db
from ..controllers.movie import get_movie, get_movies

from ..schemas.movie import Movie, MovieCreate

router = APIRouter(
    prefix="/movies",
)


@router.get("/", response_model=list[Movie])
def read_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = get_movies(db, skip=skip, limit=limit)
    return movies

@router.get("/{movie_id}", response_model=Movie)
def read_movies(id: int, db: Session = Depends(get_db)):
    movie = get_movie(db, id=id)
    return movie