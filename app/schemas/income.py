from datetime import datetime

from pydantic import BaseModel, Field
from typing import Optional


class Income(BaseModel):
    id: Optional[int] = Field(None)
    user_id: Optional[int] = Field(None)
    amount: float = Field(..., max_digits=10, decimal_places=2)
    source: str = Field(..., min_length=1)
    date: datetime = Field(...)
    created_at : Optional[datetime] = Field(None)
    updated_at: Optional[datetime] = Field(None)

