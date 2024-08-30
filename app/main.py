from fastapi import FastAPI

from app.routers import user, expense

app = FastAPI()

app.include_router(user.router, prefix="/users")
app.include_router(expense.router, prefix="/expenses")
