from datetime import datetime

from fastapi import HTTPException

from app.firebase_config import firestore_db
from app.schemas.income import Income


async def add_income(income: Income, current_user: dict):
    try:
        income.user_id = current_user["uid"]
        income.created_at = datetime.now()
        income.created_at = datetime.now()
        income_ref = firestore_db.collection("incomes").document()

        income.id = income_ref.id

        income_ref.set(income.model_dump())

        return {"message": "Income added successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
