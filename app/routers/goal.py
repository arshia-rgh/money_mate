from fastapi import APIRouter, Depends

from app.crud.goal import add_goal, delete_goal
from app.dependencies import get_current_user
from app.schemas.goal import Goal

router = APIRouter()


@router.post("/add")
async def add_goal_entry(goal: Goal, current_user: dict = Depends(get_current_user)):
    return await add_goal(goal, current_user)


@router.delete("/delete/{goal_id}")
async def delete_goal_entry(goal_id: str, current_user: dict = Depends(get_current_user)):
    return await delete_goal(goal_id, current_user)
