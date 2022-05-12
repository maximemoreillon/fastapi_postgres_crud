from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..main import get_db
from ..controllers.director import create_director, get_director, get_directors 
from ..schemas.director import Director, DirectorCreate
from ..schemas.movie import Movie, MovieCreate

router = APIRouter()



@router.post("/directors/", response_model=Director)
def create_user(director: DirectorCreate, db: Session = Depends(get_db)):
    return create_director(db=db, director=director)


@router.get("/directors/", response_model=List[Director])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    directors = get_directors(db, skip=skip, limit=limit)
    return directors


@router.get("/directors/{director_id}", response_model=Director)
def read_user(id: int, db: Session = Depends(get_db)):
    db_user = get_director(db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/directors/{director_id}/movies/", response_model=Movie)
def create_item_for_user( user_id: int, item: MovieCreate, db: Session = Depends(get_db) ):
    return crud.create_user_item(db=db, item=item, user_id=user_id)
