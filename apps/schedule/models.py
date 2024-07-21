from typing import TYPE_CHECKING, List

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.model_base import Base

if TYPE_CHECKING:
    from apps.booking.models import Booking
    from apps.movie.models import Movie
    from apps.room.models import Room


class Schedule(Base):
    __tablename__ = 'schedules'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    room_id: Mapped[int] = mapped_column(ForeignKey('rooms.id', ondelete='CASCADE'), nullable=False)
    movie_id: Mapped[int] = mapped_column(ForeignKey('movies.id', ondelete='CASCADE'), nullable=False)
    start_time: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False)
    end_time: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False)

    room: Mapped['Room'] = relationship(back_populates='movies')
    movie: Mapped['Movie'] = relationship(back_populates='rooms')
    bookings: Mapped[List['Booking']] = relationship('Booking', back_populates='schedule')
