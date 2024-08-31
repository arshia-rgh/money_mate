from app.crud.items import ExpenseCRUD, BudgetCRUD, GoalCRUD, IncomeCRUD, InvestmentCRUD, TransactionCRUD

expense_router = ExpenseCRUD().router

budget_router = BudgetCRUD().router

goal_router = GoalCRUD().router

income_router = IncomeCRUD().router

investment_router = InvestmentCRUD().router

transaction_router = TransactionCRUD().router
