from datetime import datetime

from fastapi import HTTPException

from app.firebase_config import firestore_db
from app.schemas.budget import Budget


async def add_budget(budget: Budget, current_user: dict):
    try:
        budget.user_id = current_user["uid"]
        budget.created_at = datetime.now()
        budget.updated_at = datetime.now()

        budget_ref = firestore_db.collection("budgets").document()

        budget.id = budget_ref.id

        budget_ref.set(budget.model_dump())
        return {"message": "Budget added successfully", "id": budget.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


async def delete_budget(budget_id: str, current_user: dict):
    try:
        budget_ref = firestore_db.collection("budgets").document(budget_id)
        budget = budget_ref.get().to_dict()

        if budget["user_id"] != current_user["uid"]:
            raise HTTPException(status_code=403, detail="You can only delete your own budget")

        budget_ref.delete()

        return {"message": "The budget has been successfully deleted"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


async def update_budget(budget_id: str, budget: Budget, current_user: dict):
    try:
        budget_ref = firestore_db.collection("budgets").document(budget_id)

        exists_budget = budget_ref.get().to_dict()

        if exists_budget["user_id"] != current_user["uid"]:
            raise HTTPException(status_code=403, detail="You can only modify your own budget")

        budget.created_at = exists_budget["created_at"]  # if the user tried to change the created at
        budget.user_id = current_user["uid"]
        budget.updated_at = datetime.now()
        budget_ref.update(budget.model_dump())
        return {"message": "The budget has been successfully updated"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


async def retrieve_budget(budget_id: str, current_user: dict):
    try:
        budget_ref = firestore_db.collection("budgets").document(budget_id)
        budget = budget_ref.get().to_dict()

        if budget["user_id"] != current_user["uid"]:
            raise HTTPException(status_code=403, detail="You can only access your own budget")
        return budget
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
