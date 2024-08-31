from fastapi import FastAPI

from app.routers import user, items

app = FastAPI()
app.include_router(user.router, prefix="/users")
app.include_router(items.expense_router, prefix="/expenses")
app.include_router(items.budget_router, prefix="/budgets")
app.include_router(items.goal_router, prefix="/goals")
app.include_router(items.income_router, prefix="/incomes")
app.include_router(items.investment_router, prefix="/investments")
app.include_router(items.transaction_router, prefix="/transactions")
