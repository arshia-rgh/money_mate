from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Notification(BaseModel):
    id: Optional[str] = Field(None)
    user_id: Optional[str] = Field(None)
    title: str = Field(..., min_length=1)
    message: str = Field(..., min_length=1)
    read: bool = Field(default=False)
    created_at: Optional[datetime] = Field(None)
    updated_at: Optional[datetime] = Field(None)
