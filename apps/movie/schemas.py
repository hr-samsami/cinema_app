from datetime import datetime
from typing import List

from pydantic import BaseModel

from apps.schedule.schemas import Schedule


class MovieBase(BaseModel):
    title: str
    poster: str


class MovieCreate(MovieBase):
    pass


class MovieUpdate(MovieBase):
    pass


class Movie(MovieBase):
    id: int

    class ConfigDict:
        from_attributes = True
