from datetime import datetime
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from apps.room.exceptions import NoUpcomingMoviesFoundException
from apps.movie.models import Movie
from apps.movie.schemas import MovieSchedule
from apps.room.models import Room
from apps.room.schemas import RoomCreate, RoomUpdate
from apps.schedule.models import Schedule


async def get_room(db: AsyncSession, room_id: int):
    return await db.get(Room, room_id)

async def get_rooms(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Room).offset(skip).limit(limit))
    return result.scalars().all()

async def create_room(db: AsyncSession, room: RoomCreate):
    db_room = Room(**room.model_dump())
    db.add(db_room)
    await db.commit()
    await db.refresh(db_room)
    return db_room


async def update_room(db: AsyncSession, room_id: int, room: RoomUpdate):
    db_room = await get_room(db, room_id)
    if not db_room:
        return None
    for key, value in room.model_dump(exclude_unset=True).items():
        setattr(db_room, key, value)
    await db.commit()
    await db.refresh(db_room)
    return db_room


async def delete_room(db: AsyncSession, room_id: int):
    db_room = await get_room(db, room_id)
    if not db_room:
        return False
    await db.delete(db_room)
    await db.commit()
    return True


async def get_movies_in_room(db: AsyncSession, room_id: int):
    query = (
            select(
                Movie.id,
                Movie.title,
                Movie.poster,
                Schedule.start_time,
                Schedule.end_time
            )
            .join(Schedule, Schedule.movie_id == Movie.id)
            .filter(
                Schedule.room_id == room_id,
                Schedule.start_time > datetime.now()
            )
            .distinct()
        )

    result = await db.execute(query)
    movie_schedules = result.all()
    
    if not movie_schedules:
        raise NoUpcomingMoviesFoundException()

    movies = [
        MovieSchedule(
            id=row.id,
            title=row.title,
            poster=row.poster,
            start_time=row.start_time,
            end_time=row.end_time
        )
        for row in movie_schedules
    ]

    return movies