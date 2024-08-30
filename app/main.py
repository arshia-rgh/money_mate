from fastapi import FastAPI

from app.routers import user, expense, budget, income

app = FastAPI()

app.include_router(user.router, prefix="/users")
app.include_router(expense.router, prefix="/expenses")
app.include_router(budget.router, prefix="/budgets")
app.include_router(income.router, prefix="/incomes")
