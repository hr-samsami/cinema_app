from typing import TYPE_CHECKING

from sqlalchemy import UUID, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.model_base import Base

if TYPE_CHECKING:
    from apps.schedule.models import Schedule


class Booking(Base):
    __tablename__ = 'bookings'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), index=True)
    schedule_id: Mapped[int] = mapped_column(ForeignKey('schedules.id', ondelete='CASCADE'), nullable=False)
    row_number: Mapped[int] = mapped_column(Integer)
    seat_number: Mapped[int] = mapped_column(Integer)

    __table_args__ = (
        UniqueConstraint('schedule_id', 'row_number', 'seat_number', name='uix_booking_schedule_row_seat'),
    )

    schedule: Mapped['Schedule'] = relationship(back_populates='bookings')
