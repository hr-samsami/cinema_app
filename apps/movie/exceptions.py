from typing import Any

from fastapi import status

from core.exceptions import DetailedHTTPException


class MovieNotFoundException(DetailedHTTPException):
    ERROR_CODE = 40402
    MESSAGE = 'Movie not found'
    STATUS_CODE = status.HTTP_404_NOT_FOUND
