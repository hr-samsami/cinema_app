from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from apps.booking.cruds import get_bookings
from apps.booking.schemas import Booking, SeatAvailability
from apps.movie.models import Movie
from core.dependencies import get_db

router = APIRouter()
