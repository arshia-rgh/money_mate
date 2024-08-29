from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class UserCreate(BaseModel):
    first_name: Optional[str] = Field(None)
    last_name: Optional[str] = Field(None)
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=8)


class UserLogin(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=8)
