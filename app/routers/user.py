from fastapi import APIRouter

from app.crud.user import create_user, login_user
from app.schemas.user import UserCreate, UserLogin

router = APIRouter()


@router.post("/signup")
async def signup(user: UserCreate):
    return await create_user(user)


@router.post("/login")
async def login(user: UserLogin):
    return await login_user(user)
