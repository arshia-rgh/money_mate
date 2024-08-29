from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Expense(BaseModel):
    id: Optional[str]
    user_id: Optional[str]
    category: str
    amount: float
    description: Optional[str]
    date: datetime