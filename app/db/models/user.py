# from app.db.models.base import BaseDBModel
# from pydantic import EmailStr
# from enum import Enum

# class FeedbackSource(str, Enum):
#     CHROME_EXTENSION = "CHROME_EXTENSION"
#     WEBSITE = "WEBSITE"

# class FeedbackCreate(BaseDBModel):
#     title: str
#     type: str
#     content: str
#     email: EmailStr
#     source: FeedbackSource

# class FeedbackInDB(FeedbackCreate):
#     pass