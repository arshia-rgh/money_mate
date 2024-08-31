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

    async def delete_item(self, item_id: str, current_user: dict):
        try:
            item_ref = firestore_db.collection(f"{self.collection_name}").document(item_id)

            item = item_ref.get().to_dict()

            if not item:
                raise HTTPException(status_code=404, detail=f"{self.collection_name.capitalize()} not exists")

            if item["user_id"] != current_user["uid"]:
                raise HTTPException(status_code=403, detail=f"You can only delete your own {self.collection_name}")

            item_ref.delete()
            return {"message": f"{self.collection_name.capitalize()} has been successfully deleted"}

        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def update_item(self, item_id: str, item: T, current_user: dict):
        try:
            item_ref = firestore_db.collection(f"{self.collection_name}").document(item_id)

            exists_item = item_ref.get().to_dict()

            if not exists_item:
                raise HTTPException(status_code=404, detail=f"{self.collection_name.capitalize()} not exists")

            if exists_item["user_id"] != current_user["uid"]:
                raise HTTPException(status_code=403, detail=f"You can only modify your own {self.collection_name}")

            item.user_id = current_user["uid"]
            item.created_at = exists_item["created_at"]
            item.updated_at = datetime.now()
            item.id = item_ref.id

            item_ref.update(item.model_dump())

            return {"message": f"{self.collection_name.capitalize()} has been successfully updated"}

        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def retrieve_item(self):
        pass

    async def list_items(self):
        pass
