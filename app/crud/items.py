from app.schemas import budget, expense, goal, income, investment

from .base import BaseCRUD


class ExpenseCRUD(BaseCRUD[expense.Expense]):
    def __init__(self):
        super().__init__(expense.Expense, "expenses")


class BudgetCRUD(BaseCRUD[budget.Budget]):
    def __init__(self):
        super().__init__(budget.Budget, "budgets")


class GoalCRUD(BaseCRUD[goal.Goal]):
    def __init__(self):
        super().__init__(goal.Goal, "goals")


class IncomeCRUD(BaseCRUD[income.Income]):
    def __init__(self):
        super().__init__(income.Income, "incomes")


class InvestmentCRUD(BaseCRUD[investment.Investment]):
    def __init__(self):
        super().__init__(investment.Investment, "investments")
