from typing import List, Tuple
from uuid import UUID

from pydantic import BaseModel, Field


class BookingBase(BaseModel):
    user_id: UUID
    schedule_id: int
    row_number: int = Field(gt=0)
    seat_number: int = Field(gt=0)


class BookingCreate(BookingBase):
    pass


class BookingUpdate(BookingBase):
    pass


class Booking(BookingBase):
    id: int

    class ConfigDict:
        from_attributes = True


ROW_NUMBER = int
SEAT_NUMBER = int


class SeatAvailability(BaseModel):
    schedule_id: int
    booked_seats: List[Tuple[ROW_NUMBER, SEAT_NUMBER]]
    rows: int
    seats_per_row: int
    total_seats: int

    class ConfigDict:
        from_attributes = True
