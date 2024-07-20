from typing import Any
from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

class DetailedHTTPException(HTTPException):
    ERROR_CODE = 10000
    MESSAGE = 'Server error'
    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, message: str | None = None, **kwargs: dict[str, Any]) -> None:
        message = message if message else self.MESSAGE
        detail = {'message': message, 'code': self.ERROR_CODE}
        super().__init__(status_code=self.STATUS_CODE, detail=detail, **kwargs)
        
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