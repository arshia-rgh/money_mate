import os

import requests
from dotenv import load_dotenv
from fastapi import HTTPException
from firebase_admin import auth

from app.schemas.user import UserCreate, UserLogin

load_dotenv()
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")


async def create_user(user: UserCreate):
    try:
        user_record = auth.create_user(
            email=user.email,
            password=user.password,
        )
        return {"message": "User created successfully", "uid": user_record.uid}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


async def login_user(user: UserLogin):
    try:
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"
        payload = {
            "email": user.email,
            "password": user.password,
            "returnSecureToken": True,
        }

        response = requests.post(url, json=payload)
        response_data = response.json()

        if response.status_code != 200:
            raise HTTPException(status_code=400,
                                detail=response_data.get("error", {}).get("message", "Invalid credentials"))

        return {"message": "Login successful", "token": response_data["idToken"]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
