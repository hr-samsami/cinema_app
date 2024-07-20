from sqlalchemy.ext.asyncio import AsyncSession

from apps.room.models import Room
from apps.room.schemas import RoomCreate, RoomUpdate


async def get_room(db: AsyncSession, room_id: int):
    return await db.get(Room, room_id)


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
