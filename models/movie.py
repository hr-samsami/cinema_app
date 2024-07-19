from typing import TYPE_CHECKING, List

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.booking import Booking

if TYPE_CHECKING:
    from models.schedule import Schedule


class Movie(Base):
    __tablename__ = 'movies'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    poster: Mapped[str] = mapped_column(String, nullable=False)

    rooms: Mapped[List["Schedule"]] = relationship(back_populates="movie")
