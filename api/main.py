from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.exc import IntegrityError

from api.dependencies.exceptions import (
    booking_not_found_exception_handler,
    integrity_exception_handler,
    movie_not_found_exception_handler,
    room_not_found_exception_handler,
)
from api.exceptions import (
    BookingNotFoundException,
    MovieNotFoundException,
    RoomNotFoundException,
)
from api.v1.endpoints import bookings, movies, rooms, schedules
from core.init_db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.add_exception_handler(RoomNotFoundException, room_not_found_exception_handler)
app.add_exception_handler(MovieNotFoundException, movie_not_found_exception_handler)
app.add_exception_handler(BookingNotFoundException, booking_not_found_exception_handler)
app.add_exception_handler(IntegrityError, integrity_exception_handler)


app.include_router(rooms.router, prefix='/rooms', tags=['rooms'])
app.include_router(movies.router, prefix='/movies', tags=['movies'])
app.include_router(bookings.router, prefix='/bookings', tags=['bookings'])
app.include_router(schedules.router, prefix="/schedules", tags=["schedules"])



@app.get('/')
async def read_root():
    return {'message': 'Welcome to the Cinema API'}
