from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Investment(BaseModel):
    id: Optional[str] = Field(None)
    user_id: Optional[str] = Field(None)
    type: str = Field(..., min_length=1)
    amount: float = Field(...)
    date: datetime = Field(...)
    created_at: Optional[datetime] = Field(None)
    updated_at: Optional[datetime] = Field(None)
