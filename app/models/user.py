from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    first_name: Optional[str] = Field(None)
    last_name: Optional[str] = Field(None)
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=8)
