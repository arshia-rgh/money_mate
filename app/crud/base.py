from typing import TypeVar, Generic

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class BaseCRUD(Generic[T]):
    pass
