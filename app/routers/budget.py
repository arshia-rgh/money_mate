from fastapi import APIRouter, Depends

from app.crud.budget import add_budget, delete_budget
from app.dependencies import get_current_user
from app.schemas.budget import Budget

router = APIRouter()


@router.post("/add")
async def add_budget_entry(budget: Budget, current_user: dict = Depends(get_current_user)):
    return await add_budget(budget, current_user)


@router.delete("/delete/{budget_id}")
async def delete_budget_entry(budget_id: str, current_user: dict = Depends(get_current_user)):
    return await delete_budget(budget_id, current_user)
