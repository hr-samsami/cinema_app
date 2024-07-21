from typing import List

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from apps.movie.models import Movie
from apps.schedule.models import Schedule
from core.model_base import Base


class Room(Base):
    __tablename__ = 'rooms'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    rows: Mapped[int] = mapped_column(Integer)
    seats_per_row: Mapped[int] = mapped_column(Integer)

    movies: Mapped[List['Schedule']] = relationship(back_populates='room')
