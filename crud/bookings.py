from sqlalchemy.ext.asyncio import AsyncSession

from models.booking import Booking
from schemas.booking import BookingCreate, BookingUpdate


async def get_booking(db: AsyncSession, booking_id: int):
    return await db.get(Booking, booking_id)


async def create_booking(db: AsyncSession, booking: BookingCreate):
    db_booking = Booking(**booking.model_dump())
    db.add(db_booking)
    await db.commit()
    await db.refresh(db_booking)
    return db_booking


async def update_booking(db: AsyncSession, booking_id: int, booking: BookingUpdate):
    db_booking = await get_booking(db, booking_id)
    if not db_booking:
        return None
    for key, value in booking.model_dump(exclude_unset=True).items():
        setattr(db_booking, key, value)
    await db.commit()
    await db.refresh(db_booking)
    return db_booking


async def delete_booking(db: AsyncSession, booking_id: int):
    db_booking = await get_booking(db, booking_id)
    if not db_booking:
        return False
    await db.delete(db_booking)
    await db.commit()
    return True
