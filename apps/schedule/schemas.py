# cinema_app/schemas/schedule.py

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from apps.booking.schemas import Booking


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

    class ConfigDict:
        from_attributes = True


class MovieSchedule(BaseModel):
    schedule_id: int
    title: str
    poster: str
    start_time: datetime
    end_time: datetime
