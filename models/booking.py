from typing import TYPE_CHECKING

from sqlalchemy import UUID, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base

if TYPE_CHECKING:
    from models.schedule import Schedule


class Booking(Base):
    __tablename__ = 'bookings'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), index=True)
    schedule_id: Mapped[int] = mapped_column(ForeignKey("schedules.id", ondelete="CASCADE"), nullable=False)
    row_number: Mapped[int] = mapped_column(Integer)
    seat_number: Mapped[int] = mapped_column(Integer)

    schedule: Mapped["Schedule"] = relationship(back_populates="bookings")
