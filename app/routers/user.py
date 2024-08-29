from fastapi import APIRouter, Depends

from app.crud.user import create_user, login_user, delete_user, update_user
from app.dependencies import get_current_user
from app.schemas.user import UserCreate, UserLogin

router = APIRouter()


@router.post("/signup")
async def signup(user: UserCreate):
    return await create_user(user)


@router.post("/login")
async def login(user: UserLogin):
    return await login_user(user)


@router.delete("/delete")
async def delete_account(user_id: str, current_user: dict = Depends(get_current_user)):
    return await delete_user(user_id, current_user)


@router.patch("/update")
async def update_account(user_id: str, user: UserCreate, current_user: dict = Depends(get_current_user)):
    return await update_user(user_id, user, current_user)


@router.get("/profile")
async def retrieve_account(user_id: str, current_user: dict = Depends(get_current_user)):
    return await retrieve_account(user_id, current_user)
