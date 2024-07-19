# cinema_app/schemas/schedule.py

from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from schemas.booking import Booking

class ScheduleBase(BaseModel):
    room_id: int
    movie_id: int
    start_time: datetime
    end_time: datetime

class ScheduleCreate(ScheduleBase):
    pass

class ScheduleUpdate(ScheduleBase):
    pass

class Schedule(ScheduleBase):
    id: int
    bookings: List["Booking"] = []

    class Config:
        orm_mode = True
