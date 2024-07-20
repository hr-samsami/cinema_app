from pydantic import BaseModel, Field
from typing import List

from schemas.schedule import Schedule

class RoomBase(BaseModel):
    name: str
    rows: int = Field(gt=0)
    seats_per_row: int = Field(gt=0)

class RoomCreate(RoomBase):
    pass

class RoomUpdate(RoomBase):
    pass

class Room(RoomBase):
    id: int
    schedules: List["Schedule"] = []

    class Config:
        orm_mode = True
