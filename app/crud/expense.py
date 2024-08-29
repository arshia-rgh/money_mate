from fastapi import HTTPException

from app.firebase_config import db
from app.schemas.expense import Expense


async def add_expense(expense: Expense, current_user: dict):
    try:
        expense.user_id = current_user["uid"]
        expense_ref = db.collection("expenses").document()
        expense.id = expense_ref.id
        expense_ref.set(expense.model_dump())

        return {"message": "Expense added successfully", "id": expense.id}
    except Expense as e:
        raise HTTPException(status_code=400, detail=str(e))
