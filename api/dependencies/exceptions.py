from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from api.exceptions import BookingNotFoundException, MovieNotFoundException, RoomNotFoundException, ScheduleNotFoundException

async def room_not_found_exception_handler(request: Request, exc: RoomNotFoundException):
    return JSONResponse(status_code=404, content={"message": exc.detail})

async def movie_not_found_exception_handler(request: Request, exc: MovieNotFoundException):
    return JSONResponse(status_code=404, content={"message": exc.detail})

async def booking_not_found_exception_handler(request: Request, exc: BookingNotFoundException):
    return JSONResponse(status_code=404, content={"message": exc.detail})

async def schedule_not_found_exception_handler(request: Request, exc: ScheduleNotFoundException):
    return JSONResponse(status_code=404, content={"message": exc.detail})

async def integrity_exception_handler(request: Request, exc: IntegrityError):
    detail = 'Integrity error: constraint violation.'

    error_message = str(exc.orig)
    if 'violates foreign key constraint' in error_message:
        detail = 'Integrity error: foreign key violation.'
    elif 'violates unique constraint' in error_message:
        detail = 'Integrity error: duplicate entry.'
    elif 'null value in column' in error_message:
        detail = 'Integrity error: not-null constraint violation.'
    elif 'violates check constraint' in error_message:
        detail = 'Integrity error: check constraint violation.'

    return JSONResponse(
        status_code=400,
        content={'detail': detail},
    )