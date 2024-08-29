from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Expense(BaseModel):
    id: Optional[str] = Field(None)
    user_id: Optional[str] = Field(None)
    category: str = Field(...)
    amount: float = Field(...)
    description: Optional[str] = Field(None)
    date: Optional[datetime] = Field(None)
