from fastapi import FastAPI, BackgroundTasks

from app.routers import user, items
from app.utils.notifications import NotificationHandle

app = FastAPI()


@app.post("/start-notifications/{user_id}/")
async def start_notifications(user_id: str, background_tasks: BackgroundTasks):
    notification_crud = NotificationHandle(user_id)
    notification_crud.start_listening(background_tasks)

    return {"message": "Started listening for new notifications"}


app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(items.expense_router, prefix="/expenses", tags=["expenses"])
app.include_router(items.budget_router, prefix="/budgets", tags=["budgets"])
app.include_router(items.goal_router, prefix="/goals", tags=["goals"])
app.include_router(items.income_router, prefix="/incomes", tags=["incomes"])
app.include_router(items.investment_router, prefix="/investments", tags=["investments"])
app.include_router(items.transaction_router, prefix="/transactions", tags=["transactions"])
