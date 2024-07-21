from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from apps.booking.cruds import create_booking, delete_booking, get_booking, update_booking
from apps.booking.exceptions import BookingNotFoundException
from apps.booking.schemas import Booking, BookingCreate, BookingUpdate
from core.dependencies import get_db

router = APIRouter()


@router.get('/{booking_id}', response_model=Booking)
async def read_booking(booking_id: int, db: AsyncSession = Depends(get_db)):
    db_booking = await get_booking(db, booking_id)
    if not db_booking:
        raise BookingNotFoundException()
    return db_booking


@router.post('/', response_model=Booking)
async def create_new_booking(booking: BookingCreate, db: AsyncSession = Depends(get_db)):
    return await create_booking(db, booking)


@router.put('/{booking_id}', response_model=Booking)
async def update_existing_booking(booking_id: int, booking: BookingUpdate, db: AsyncSession = Depends(get_db)):
    db_booking = await update_booking(db, booking_id, booking)
    if not db_booking:
        raise BookingNotFoundException()
    return db_booking


@router.delete('/{booking_id}', response_model=bool)
async def delete_existing_booking(booking_id: int, db: AsyncSession = Depends(get_db)):
    success = await delete_booking(db, booking_id)
    if not success:
        raise BookingNotFoundException()
    return True
