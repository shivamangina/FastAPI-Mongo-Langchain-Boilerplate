from typing import List
from fastapi import APIRouter, Depends, Body
from app.db.database import get_db
from datetime import datetime
from app.db.models.feedback import Feedback



router = APIRouter(
    prefix="/feedback",
    tags=["feedback"],
)


@router.get("", response_model=List[Feedback], tags=["feedback"])
async def get_all_feedback(db=Depends(get_db)):
    feedbacks = db.feedbacks.find().to_list(length=None)
    if feedbacks is None:
        return []
    return [Feedback(**{**feedback, "_id": str(feedback["_id"])}) for feedback in feedbacks]
 


@router.post("",response_model=str, tags=["feedback"])
async def create_feedback(feedback: Feedback = Body(...),
                          db=Depends(get_db)):
    feedback_dict = feedback.dict(exclude_unset=True)
    feedback_dict["createdAt"] = datetime.now()
    feedback_dict["updatedAt"] = datetime.now()
    result = db.feedbacks.insert_one(feedback_dict)
    return str(result.inserted_id)
