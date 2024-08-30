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
