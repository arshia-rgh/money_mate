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


async def delete_income(income_id: str, current_user: dict):
    try:
        income_ref = firestore_db.collection("incomes").document(income_id)

        income = income_ref.get().to_dict()

        if income["user_id"] != current_user["uid"]:
            raise HTTPException(status_code=403, detail="You can only delete your own income")

        income_ref.delete()

        return {"message": "Income deleted successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
