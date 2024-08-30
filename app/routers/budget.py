from fastapi import APIRouter, Depends

from app.crud.budget import add_budget
from app.dependencies import get_current_user
from app.schemas.budget import Budget

router = APIRouter()


@router.post("/add")
async def add_budget_entry(budget: Budget, current_user: dict = Depends(get_current_user))
    return await add_budget(budget, current_user)
