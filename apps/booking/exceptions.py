from fastapi import status

from core.exceptions import DetailedHTTPException


class BookingNotFoundException(DetailedHTTPException):
    ERROR_CODE = 40403
    MESSAGE = 'Booking not found'
    STATUS_CODE = status.HTTP_404_NOT_FOUND
