from http import HTTPStatus
from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class Response(BaseModel, Generic[T]):
    data: T
    status: HTTPStatus


__all__ = [
    "Response",
]
