from fastapi import APIRouter, Depends

from app.crud.expense import add_expense, delete_expense, update_expense, retrieve_expense, list_expense
from app.dependencies import get_current_user
from app.schemas.expense import Expense

router = APIRouter()


@router.post("/add")
async def add_expense_entry(expense: Expense, current_user: dict = Depends(get_current_user)):
    return await add_expense(expense, current_user)


@router.delete("/delete")
async def delete_expense_entry(expense_id: str, current_user: dict = Depends(get_current_user)):
    return await delete_expense(expense_id, current_user)


@router.patch("/update")
async def update_expense_entry(expense_id: str, expense: Expense, current_user: dict = Depends(get_current_user)):
    return await update_expense(expense_id, expense, current_user)


@router.get("/retrieve")
async def retrieve_expense_entry(expense_id: str, current_user: dict = Depends(get_current_user)):
    return await retrieve_expense(expense_id, current_user)


@router.get("/list")
async def list_expenses_entry(current_user: dict = Depends(get_current_user)):
    return await list_expense(current_user)
