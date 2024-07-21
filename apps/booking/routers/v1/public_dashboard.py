from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apps.booking.cruds import get_bookings
from apps.booking.schemas import Booking
from core.dependencies import get_db

router = APIRouter()
