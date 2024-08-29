from google.cloud import firestore

from app.schemas.expense import Expense

db = firestore.Client()


async def add_expense(expense: Expense, current_user: dict):
    pass
