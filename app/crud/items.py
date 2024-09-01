from app.schemas import budget, expense, goal, income, investment, transaction

from .base import BaseCRUD

expense_crud = BaseCRUD(expense.Expense, "expenses")
budget_crud = BaseCRUD(budget.Budget, "budgets")
goal_crud = BaseCRUD(goal.Goal, "goals")
income_crud = BaseCRUD(income.Income, "incomes")
invest_crud = BaseCRUD(investment.Investment, "investments")
transaction_crud = BaseCRUD(transaction.Transaction, "transactions")
