from fastapi import FastAPI, HTTPException
import firebase_config
from firebase_admin import auth
from schemas.user import UserLogin, UserCreate

app = FastAPI()


@app.post("/signup")
async def signup(user: UserCreate):
    try:
        user_record = auth.create_user(
            email=user.email,
            password=user.password,
        )

        return {"message": "User created successfully", "uid": user_record.uid}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
