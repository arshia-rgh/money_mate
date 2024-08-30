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


async def delete_goal(goal_id: str, current_user: dict):
    try:
        goal_ref = firestore_db.collection("goals").document(goal_id)
        goal = goal_ref.get().to_dict()

        if goal["user_id"] != current_user["uid"]:
            raise HTTPException(status_code=403, detail="You can only delete your own goal")

        goal_ref.delete()

        return {"message": "The goal has been deleted successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


async def update_goal(goal_id: str, goal: Goal, current_user: dict):
    try:
        goal_ref = firestore_db.collection("goals").document(goal_id)

        exists_goal = goal_ref.get().to_dict()

        if exists_goal["user_id"] != current_user["uid"]:
            raise HTTPException(status_code=403, detail="You can only modify your own goal")

        goal.user_id = current_user["uid"]
        goal.created_at = exists_goal["created_at"]
        goal.updated_at = datetime.now()

        goal_ref.update(goal.model_dump())

        return {"message": "The goal updated successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


async def retrieve_goal(goal_id: str, current_user: dict):
    try:
        goal_ref = firestore_db.collection("goals").document(goal_id)

        goal = goal_ref.get().to_dict()

        if goal["user_id"] != current_user["uid"]:
            raise HTTPException(status_code=403, detail="You can only access your own goal")
        return goal

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


async def list_goal(current_user: dict):
    try:
        goals_ref = firestore_db.collection("goals").where("user_id", "==", current_user["uid"])

        goals = goals_ref.stream()

        goals_list = [goal.to_dict() for goal in goals]

        return goals_list

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
