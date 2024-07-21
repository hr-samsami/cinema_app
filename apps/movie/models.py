from typing import TYPE_CHECKING, List

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from apps.booking.models import Booking
from core.model_base import Base

if TYPE_CHECKING:
    from apps.schedule.models import Schedule


class Movie(Base):
    __tablename__ = 'movies'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    poster: Mapped[str] = mapped_column(String, nullable=False)

    rooms: Mapped[List['Schedule']] = relationship(back_populates='movie')
