from typing import Optional

from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    summary: Optional[str] = None


class MovieCreate(MovieBase):
    pass


class Movie(MovieBase):
    id: int
    director_id: int

    class Config:
        orm_mode = True
