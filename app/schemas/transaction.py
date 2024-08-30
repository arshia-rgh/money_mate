from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Transaction(BaseModel):
    id: Optional[int] = Field(None)
    user_id: Optional[int] = Field(None)
    type: str = Field(...)  # 'income' or 'expense'
    amount: float = Field(..., max_digits=10, decimal_places=2)
    category: str = Field(...)
    description: Optional[str] = Field(None)
    date: datetime = Field(...)
    created_at: Optional[datetime] = Field(None)
    updated_at: Optional[datetime] = Field(None)
