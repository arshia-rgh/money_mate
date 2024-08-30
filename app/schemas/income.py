from datetime import datetime

from pydantic import BaseModel, Field
from typing import Optional


class Income(BaseModel):
    id: Optional[str] = Field(None)
    user_id: Optional[str] = Field(None)
    amount: float = Field(...)
    source: str = Field(..., min_length=1)
    date: datetime = Field(...)
    created_at : Optional[datetime] = Field(None)
    updated_at: Optional[datetime] = Field(None)

