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

    class Config:
        orm_mode = True
