from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.exc import IntegrityError

from apps.booking.routers.v1.admin_dashboard import router as admin_booking_router
from apps.movie.routers.v1.admin_dashboard import router as admin_movie_router
from apps.room.routers.v1.admin_dashboard import router as admin_room_router
from apps.schedule.routers.v1.admin_dashboard import router as admin_schedule_router
from core.exceptions import integrity_exception_handler
from core.init_db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.add_exception_handler(IntegrityError, integrity_exception_handler)


app.include_router(admin_room_router, prefix='/rooms', tags=['rooms'])
app.include_router(admin_movie_router, prefix='/movies', tags=['movies'])
app.include_router(admin_booking_router, prefix='/bookings', tags=['bookings'])
app.include_router(admin_schedule_router, prefix='/schedules', tags=['schedules'])


@app.get('/')
async def read_root():
    return {'message': 'Welcome to the Cinema API'}
