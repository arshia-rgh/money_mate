from fastapi import APIRouter, Depends

from app.crud.expense import add_expense
from app.dependencies import get_current_user
from app.schemas.expense import Expense

router = APIRouter()


@router.post("/add")
async def add_expense_entry(expense: Expense, current_user: dict = Depends(get_current_user)):
    return await add_expense(expense, current_user)
