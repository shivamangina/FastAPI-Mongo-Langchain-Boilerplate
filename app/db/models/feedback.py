from app.db.models.base import BaseDBModel
from pydantic import EmailStr
from enum import Enum
from datetime import datetime
from typing import Optional

class FeedbackSource(str, Enum):
    CHROME_EXTENSION = "CHROME_EXTENSION"
    WEBSITE = "WEBSITE"

class Feedback(BaseDBModel):
    _id: str
    title: str
    type: str
    content: str
    email: EmailStr
    source: FeedbackSource
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    
    


    