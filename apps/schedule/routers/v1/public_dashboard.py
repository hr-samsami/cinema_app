from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from apps.booking.cruds import get_bookings
from apps.booking.models import Booking
from apps.booking.schemas import SeatAvailability
from apps.schedule.exceptions import ScheduleNotFoundException
from apps.schedule.models import Schedule
from core.dependencies import get_db

router = APIRouter()


@router.get('/{schedule_id}/seats', response_model=SeatAvailability)
async def get_seat_availability(schedule_id: int, db: AsyncSession = Depends(get_db)):
    query = select(Schedule).options(selectinload(Schedule.room)).where(Schedule.id == schedule_id)
    result = await db.execute(query)
    schedule = result.scalars().first()
    if schedule is None:
        raise ScheduleNotFoundException()
    result = await db.execute(select(Booking).where(Booking.schedule_id == schedule_id))
    bookings = result.scalars().all()
    booked_seats = [(booking.row_number, booking.seat_number) for booking in bookings]

    return SeatAvailability(
        schedule_id=schedule_id,
        booked_seats=booked_seats,
        rows=schedule.room.rows,
        seats_per_row=schedule.room.seats_per_row,
        total_seats=schedule.room.total_seats,
    )
