from datetime import datetime

from fastapi import HTTPException

from app.firebase_config import db
from app.schemas.expense import Expense


async def add_expense(expense: Expense, current_user: dict):
    try:
        expense.user_id = current_user["uid"]
        expense.date = datetime.now()
        expense_ref = db.collection("expenses").document()
        expense.id = expense_ref.id
        expense_ref.set(expense.model_dump())

        return {"message": "Expense added successfully", "id": expense.id}
    except Expense as e:
        raise HTTPException(status_code=400, detail=str(e))


async def delete_expense(expense_id: str, current_user: dict):
    try:
        expense_ref = db.collection("expenses").document(expense_id)
        expense = expense_ref.get().to_dict()
        if expense["user_id"] != current_user["uid"]:
            raise HTTPException(status_code=403,
                                detail="Permission Denied, You can only delete your expenses not others")

        expense_ref.delete()
        return {"message": "Expense deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


async def update_expense(expense_id: str, current_user: dict):
    pass


async def get_expense(expense_id: str, current_user: dict):
    pass
