from app.schemas import budget, expense, goal, income, investment, transaction

from .base import BaseCRUD


class ExpenseCRUD(BaseCRUD):
    def __init__(self):
        super().__init__(expense.Expense, "expenses")


class BudgetCRUD(BaseCRUD):
    def __init__(self):
        super().__init__(budget.Budget, "budgets")


class GoalCRUD(BaseCRUD):
    def __init__(self):
        super().__init__(goal.Goal, "goals")


class IncomeCRUD(BaseCRUD):
    def __init__(self):
        super().__init__(income.Income, "incomes")


class InvestmentCRUD(BaseCRUD):
    def __init__(self):
        super().__init__(investment.Investment, "investments")


class TransactionCRUD(BaseCRUD):
    def __init__(self):
        super().__init__(transaction.Transaction, "transactions")
