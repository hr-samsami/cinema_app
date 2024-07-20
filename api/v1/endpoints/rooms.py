from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.db import get_db
from api.exceptions import RoomNotFoundException
from crud.rooms import create_room, delete_room, get_room, update_room
from schemas.room import Room, RoomCreate, RoomUpdate

router = APIRouter()


@router.get('/{room_id}', response_model=Room)
async def read_room(room_id: int, db: AsyncSession = Depends(get_db)):
    db_room = await get_room(db, room_id)
    if not db_room:
        raise RoomNotFoundException()
    return db_room


@router.post('/', response_model=Room)
async def create_new_room(room: RoomCreate, db: AsyncSession = Depends(get_db)):
    return await create_room(db, room)


@router.put('/{room_id}', response_model=Room)
async def update_existing_room(room_id: int, room: RoomUpdate, db: AsyncSession = Depends(get_db)):
    db_room = await update_room(db, room_id, room)
    if not db_room:
        raise RoomNotFoundException()
    return db_room


@router.delete('/{room_id}', response_model=bool)
async def delete_existing_room(room_id: int, db: AsyncSession = Depends(get_db)):
    success = await delete_room(db, room_id)
    if not success:
        raise RoomNotFoundException()
    return True
