from pydantic import BaseModel
from typing import Any


class ErrorModel(BaseModel):
    code: int
    details: Any = None


class StandardResponse[T](BaseModel):
    status: bool
    message: str
    data: T | None = None
    error: ErrorModel | None = None


def success_response(message: str = "", data: Any = None):
    return StandardResponse(status=True, message=message, data=data).model_dump()


def error_response(code: int, message: str = "", details: Any = None):
    return StandardResponse(
        status=False, message=message, error=ErrorModel(code=code, details=details)
    ).model_dump()
