from fastapi import HTTPException
from firebase_admin import auth

from app.schemas.user import UserCreate


async def create_user(user: UserCreate):
    try:
        user_record = auth.create_user(
            email=user.email,
            password=user.password,
        )
        return {"message": "User created successfully", "uid": user_record.uid}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
