from uuid import UUID

from pydantic import BaseModel


class BookingBase(BaseModel):
    user_id: UUID
    schedule_id: int
    seat_row: int
    seat_number: int


class BookingCreate(BookingBase):
    pass


class BookingUpdate(BookingBase):
    pass


class Booking(BookingBase):
    id: int

    class Config:
        orm_mode = True
