from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class UserCreate(BaseModel):
    first_name: Optional[str] = Field(None)
    last_name: Optional[str] = Field(None)
    phone_number: str = Field(..., max_length=13)
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=8)
    created_at: Optional[datetime] = Field(None)
    updated_at: Optional[datetime] = Field(None)


class UserLogin(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=8)
