from typing import Any
from fastapi import HTTPException, status

class DetailedHTTPException(HTTPException):
    ERROR_CODE = 10000
    MESSAGE = 'Server error'
    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, message: str | None = None, **kwargs: dict[str, Any]) -> None:
        message = message if message else self.MESSAGE
        detail = {'message': message, 'code': self.ERROR_CODE}
        super().__init__(status_code=self.STATUS_CODE, detail=detail, **kwargs)
        
class RoomNotFoundException(DetailedHTTPException):
    ERROR_CODE = 40401
    MESSAGE = 'Room not found'
    STATUS_CODE = status.HTTP_404_NOT_FOUND

class MovieNotFoundException(DetailedHTTPException):
    ERROR_CODE = 40402
    MESSAGE = 'Movie not found'
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    
class BookingNotFoundException(DetailedHTTPException):
    ERROR_CODE = 40403
    MESSAGE = 'Booking not found'
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    
class ScheduleNotFoundException(DetailedHTTPException):
    ERROR_CODE = 40404
    MESSAGE = 'Schedule not found'
    STATUS_CODE = status.HTTP_404_NOT_FOUND