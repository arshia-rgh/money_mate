import os
from datetime import datetime

import requests
from dotenv import load_dotenv
from fastapi import HTTPException
from firebase_admin import auth

from app.firebase_config import db
from app.schemas.user import UserCreate, UserLogin

load_dotenv()
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")


async def create_user(user: UserCreate):
    try:
        user_record = auth.create_user(
            email=user.email,
            password=user.password,
        )
        # add full users data to the db
        user_data = {
            "uid": user_record.uid,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone_number": user.phone_number,
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        }
        db.collection("users").document(user_record.uid).set(user_data)

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


async def delete_user(user_id: str, current_user: dict):
    try:
        user_ref = db.collection("users").document(user_id)
        user = user_ref.get().to_dict()

        if user["uid"] != current_user["uid"]:
            raise HTTPException(status_code=403, detail="You can only delete your own account not others")

        auth.delete_user(user_id)

        user_ref.delete()
        return {"message": "Your user deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


async def update_user(user_id: str, user: UserCreate, current_user: dict):
    try:
        user_ref = db.collection("users").document(user_id)
        exists_user = user_ref.get().to_dict()

        if exists_user["uid"] != current_user["uid"]:
            raise HTTPException(status_code=403, detail="You can only edit your own account not others")

        auth.update_user(
            user_id,
            email=user.email,
            password=user.password,
            display_name=f"{user.first_name} {user.last_name}",
            phone_number=user.phone_number,
        )

        user.updated_at = datetime.now()
        user_ref.update(user.model_dump())
        return {"message": "Your account has been updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
