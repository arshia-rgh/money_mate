from fastapi import FastAPI, BackgroundTasks

from app.routers import user, items
from app.utils.notifications import NotificationCRUD

app = FastAPI()


@app.post("/start-notifications/{user_id}/")
async def start_notifications(user_id: str, background_tasks: BackgroundTasks):
    notification_crud = NotificationCRUD(user_id)


app.include_router(user.router, prefix="/users")
app.include_router(items.expense_router, prefix="/expenses")
app.include_router(items.budget_router, prefix="/budgets")
app.include_router(items.goal_router, prefix="/goals")
app.include_router(items.income_router, prefix="/incomes")
app.include_router(items.investment_router, prefix="/investments")
app.include_router(items.transaction_router, prefix="/transactions")
