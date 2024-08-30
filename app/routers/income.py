from fastapi import APIRouter, Depends

from app.crud.income import add_income
from app.dependencies import get_current_user
from app.schemas.income import Income

router = APIRouter()


@router.post("/add")
async def add_income_entry(income: Income, current_user: dict = Depends(get_current_user)):
    return await add_income(income, current_user)
