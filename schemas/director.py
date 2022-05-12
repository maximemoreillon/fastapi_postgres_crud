from typing import List, Optional

from pydantic import BaseModel
from .movie import Movie

class DirectorBase(BaseModel):
    name: str
    age: Optional[int] = None


class DirectorCreate(DirectorBase):
    pass


class Director(DirectorBase):
    id: int
    movies: List[Movie] = []

    class Config:
        orm_mode = True