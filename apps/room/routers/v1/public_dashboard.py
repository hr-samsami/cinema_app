from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apps.movie.schemas import Movie, MovieSchedule
from apps.room.cruds import get_movies_in_room, get_rooms
from apps.room.schemas import Room
from core.dependencies import get_db

router = APIRouter()

@router.get("/", response_model=List[Room])
async def list_rooms(skip: int = 0, limit: int = 100,db: AsyncSession = Depends(get_db)):
    return await get_rooms(db,skip=skip,limit=limit)

@router.get("/{room_id}/movies", response_model=List[MovieSchedule])
async def list_movies_in_room(room_id: int, db: AsyncSession = Depends(get_db)):
    return await get_movies_in_room(db, room_id)