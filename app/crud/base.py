from datetime import datetime
from typing import TypeVar, Generic, Type

from fastapi import HTTPException
from pydantic import BaseModel

from app.firebase_config import firestore_db

T = TypeVar("T", bound=BaseModel)


class BaseCRUD(Generic[T]):
    def __init__(self, model: Type[T], collection_name: str):
        self.model = model
        self.collection_name = collection_name

    async def add_item(self, item: T, current_user: dict):
        try:
            item_ref = firestore_db.collection(f"{self.collection_name}").document()
            item.user_id = current_user["uid"]
            item.updated_at = datetime.now()
            item.created_at = datetime.now()
            item.id = item_ref.id

            item_ref.set(item.model_dump())

            return {"message": f"{self.collection_name.capitalize()} has been successfully added", "id": item.id}

        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def delete_item(self):
        pass

    async def update_item(self):
        pass

    async def retrieve_item(self):
        pass

    async def list_items(self):
        pass
