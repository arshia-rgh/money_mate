from fastapi import APIRouter

from app.crud.user import create_user
from app.schemas.user import UserCreate

router = APIRouter()


@router.post("/signup")
async def signup(user: UserCreate):
    return await create_user(user)
