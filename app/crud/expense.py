from datetime import datetime

from fastapi import HTTPException

from app.firebase_config import firestore_db
from app.schemas.expense import Expense


async def add_expense(expense: Expense, current_user: dict):
    try:
        expense.user_id = current_user["uid"]
        expense.created_at = datetime.now()
        expense.updated_at = datetime.now()
        expense_ref = firestore_db.collection("expenses").document()
        expense.id = expense_ref.id
        expense_ref.set(expense.model_dump())

        return {"message": "Expense added successfully", "id": expense.id}

    except Expense as e:
        raise HTTPException(status_code=400, detail=str(e))


async def delete_expense(expense_id: str, current_user: dict):
    try:
        expense_ref = firestore_db.collection("expenses").document(expense_id)
        expense = expense_ref.get().to_dict()

        if expense["user_id"] != current_user["uid"]:
            raise HTTPException(status_code=403,
                                detail="Permission Denied, You can only delete your expenses not others")

        expense_ref.delete()
        return {"message": "Expense deleted successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


async def update_expense(expense_id: str, expense: Expense, current_user: dict):
    try:
        expense_ref = firestore_db.collection("expenses").document(expense_id)
        exists_expense = expense_ref.get().to_dict()
        if exists_expense["user_id"] != current_user["uid"]:
            raise HTTPException(status_code=403,
                                detail="Permission Denied, You can only modify your expenses not others")

        expense.created_at = exists_expense["created_at"]
        expense.user_id = current_user["uid"]
        expense.updated_at = datetime.now()
        expense_ref.update(expense.model_dump())
        return {"message": "Expense updated successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


async def retrieve_expense(expense_id: str, current_user: dict):
    try:
        expense_ref = firestore_db.collection("expenses").document(expense_id)
        expense = expense_ref.get().to_dict()

        if expense["user_id"] != current_user["uid"]:
            raise HTTPException(status_code=403,
                                detail="Permission Denied, You can only access your expenses not others")

        return expense
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
