from typing import TypeVar, Generic, Type

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class BaseCRUD(Generic[T]):
    def __init__(self, model: Type[T], collection_name: str):
        self.model = model
        self.collection_name = collection_name

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
