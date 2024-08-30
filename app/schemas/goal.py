from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Goal(BaseModel):
    id: Optional[str] = Field(None)
    user_id: Optional[str] = Field(None)
    name: str = Field(..., min_length=1)
    target_amount: float = Field(..., max_digits=10, decimal_places=2)
    current_amount: float = Field(..., max_digits=10, decimal_places=2)
    deadline: datetime = Field(...)
    created_at: Optional[datetime] = Field(None)
    updated_at: Optional[datetime] = Field(None)
