from typing import Any

from fastapi import HTTPException, status

from core.exceptions import DetailedHTTPException


class RoomNotFoundException(DetailedHTTPException):
    ERROR_CODE = 40401
    MESSAGE = 'Room not found'
    STATUS_CODE = status.HTTP_404_NOT_FOUND
