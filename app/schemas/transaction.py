from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Transaction(BaseModel):
    id: Optional[str] = Field(None)
    user_id: Optional[str] = Field(None)
    type: str = Field(..., min_length=1)  # 'income' or 'expense'
    amount: float = Field(..., max_digits=10, decimal_places=2)
    category: str = Field(..., min_length=1)
    description: Optional[str] = Field(None)
    date: datetime = Field(...)
    created_at: Optional[datetime] = Field(None)
    updated_at: Optional[datetime] = Field(None)
