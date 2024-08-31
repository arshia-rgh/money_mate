from app.schemas import budget, expense, goal, income, investment

from .base import BaseCRUD


class ExpenseCRUD(BaseCRUD[expense.Expense]):
    def __init__(self):
        super().__init__(expense.Expense, "expenses")



