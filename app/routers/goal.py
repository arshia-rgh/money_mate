from fastapi import APIRouter, Depends

from app.crud.goal import add_goal, delete_goal, update_goal, retrieve_goal, list_goal
from app.dependencies import get_current_user
from app.schemas.goal import Goal

router = APIRouter()


@router.post("/add")
async def add_goal_entry(goal: Goal, current_user: dict = Depends(get_current_user)):
    return await add_goal(goal, current_user)


@router.delete("/delete/{goal_id}")
async def delete_goal_entry(goal_id: str, current_user: dict = Depends(get_current_user)):
    return await delete_goal(goal_id, current_user)


@router.patch("/update/{goal_id}")
async def update_goal_entry(goal_id: str, goal: Goal, current_user: dict = Depends(get_current_user)):
    return await update_goal(goal_id, goal, current_user)


@router.get("/retrieve/{goal_id}")
async def retrieve_goal_entry(goal_id: str, current_user: dict = Depends(get_current_user)):
    return await retrieve_goal(goal_id, current_user)


@router.get("/list")
async def list_goal_entry(current_user: dict = Depends(get_current_user)):
    return await list_goal(current_user)
