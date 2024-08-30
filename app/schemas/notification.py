from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Notification(BaseModel):
    id: Optional[int] = Field(None)
    user_id: Optional[int] = Field(None)
    message: str = Field(..., min_length=1)
    read: bool = Field(default=False)
    created_at: Optional[datetime] = Field(None)
    updated_at: Optional[datetime] = Field(None)