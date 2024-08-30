from datetime import datetime

from fastapi import HTTPException

from app.firebase_config import firestore_db
from app.schemas.goal import Goal


async def add_goal(goal: Goal, current_user: dict):
    try:
        goal.user_id = current_user["uid"]
        goal.created_at = datetime.now()
        goal.updated_at = datetime.now()

        goal_ref = firestore_db.collection("goals").document()

        goal.id = goal_ref.id

        goal_ref.set(goal.model_dump())

        return {"message": "The goal has been added successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
