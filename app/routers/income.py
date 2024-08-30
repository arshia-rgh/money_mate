from fastapi import APIRouter, Depends

from app.crud.income import add_income, delete_income
from app.dependencies import get_current_user
from app.schemas.income import Income

router = APIRouter()


@router.post("/add")
async def add_income_entry(income: Income, current_user: dict = Depends(get_current_user)):
    return await add_income(income, current_user)


@router.delete("/delete/{income_id}")
async def delete_income_entry(income_id: str, current_user: dict = Depends(get_current_user)):
    return await delete_income(income_id, current_user)
