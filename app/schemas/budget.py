from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Budget(BaseModel):
    id: Optional[str] = Field(None)
    user_id: Optional[str] = Field(None)
    category: str = Field(..., min_length=1)
    amount: float = Field(...)
    start_date: datetime = Field(None)
    end_date: datetime = Field(None)
    created_at: Optional[datetime] = Field(None)
    updated_at: Optional[datetime] = Field(None)
