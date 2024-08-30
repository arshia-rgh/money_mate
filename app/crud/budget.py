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
        budget_ref = firestore_db.collection("budgets").document(firestore_db)
        budget = budget_ref.get().to_dict()

        if budget["user_id"] != current_user["uid"]:
            raise HTTPException(status_code=403, detail="You can only delete your own budget")

        budget_ref.delete()

        return {"message": "The budget has been successfully deleted"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
