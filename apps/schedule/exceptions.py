from typing import Any

from fastapi import HTTPException, status

from core.exceptions import DetailedHTTPException


class ScheduleNotFoundException(DetailedHTTPException):
    ERROR_CODE = 40404
    MESSAGE = 'Schedule not found'
    STATUS_CODE = status.HTTP_404_NOT_FOUND
