from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from firebase_admin import auth

oauth2 = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Depends(oauth2)):
    try:
        decoded_token = auth.verify_id_token(token)

        return decoded_token
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
