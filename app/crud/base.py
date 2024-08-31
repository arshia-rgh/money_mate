from typing import TypeVar, Generic

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class BaseCRUD(Generic[T]):
    def __init__(self):
        pass

    async def add_item(self):
        pass

    async def delete_item(self):
        pass

    async def update_item(self):
        pass

    async def retrieve_item(self):
        pass

    async def list_items(self):
        pass
