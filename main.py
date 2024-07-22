from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI
from sqlalchemy.exc import IntegrityError

# Admin
from apps.booking.routers.v1.admin_dashboard import router as admin_booking_router

# Public
from apps.booking.routers.v1.public_dashboard import router as public_booking_router
from apps.movie.routers.v1.admin_dashboard import router as admin_movie_router
from apps.movie.routers.v1.public_dashboard import router as public_movie_router
from apps.room.routers.v1.admin_dashboard import router as admin_room_router
from apps.room.routers.v1.public_dashboard import router as public_room_router
from apps.schedule.routers.v1.admin_dashboard import router as admin_schedule_router
from apps.schedule.routers.v1.public_dashboard import router as public_schedule_router
from core.exceptions import integrity_exception_handler
from core.init_db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.add_exception_handler(IntegrityError, integrity_exception_handler)
admin_router = APIRouter(prefix='/admin')
public_router = APIRouter(prefix='/public')

# Admin routers
admin_router.include_router(admin_room_router, prefix='/rooms', tags=['rooms'])
admin_router.include_router(admin_movie_router, prefix='/movies', tags=['movies'])
admin_router.include_router(admin_booking_router, prefix='/bookings', tags=['bookings'])
admin_router.include_router(admin_schedule_router, prefix='/schedules', tags=['schedules'])
app.include_router(admin_router)

# Public routers
public_router.include_router(public_room_router, prefix='/rooms', tags=['rooms'])
public_router.include_router(public_movie_router, prefix='/movies', tags=['movies'])
public_router.include_router(public_booking_router, prefix='/bookings', tags=['bookings'])
public_router.include_router(public_schedule_router, prefix='/schedules', tags=['schedules'])
app.include_router(public_router)


@app.get('/')
async def read_root():
    return {'message': 'Welcome to the Cinema API'}
