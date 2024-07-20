from typing import TYPE_CHECKING, List
from sqlalchemy import Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base

if TYPE_CHECKING:
    from models.room import Room
    from models.movie import Movie
    from models.booking import Booking
    
class Schedule(Base):
    __tablename__ = "schedules"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id", ondelete='CASCADE'), nullable=False)
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id", ondelete='CASCADE'), nullable=False)
    start_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    end_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)

    room: Mapped["Room"] = relationship(back_populates="movies")
    movie: Mapped["Movie"] = relationship(back_populates="rooms")
    bookings: Mapped[List["Booking"]] = relationship("Booking", back_populates="schedule")
