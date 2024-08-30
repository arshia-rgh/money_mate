from fastapi import FastAPI

from app.routers import user, expense, budget

app = FastAPI()

app.include_router(user.router, prefix="/users")
app.include_router(expense.router, prefix="/expenses")
app.include_router(budget.router, prefix="/budgets")
