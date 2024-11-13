from pydantic import BaseModel
from typing import List

class CommentSummary(BaseModel):
    videoTitle: str
    topComments: List[str]


class VideoInfo(BaseModel):
    id: str
    name: str
    description: str


class ClassificationRequest(BaseModel):
    goal: str
    videos: List[VideoInfo]


class VideoClassificationResult(BaseModel):
    id: str
    name: str
    relevant: bool


class ClassificationResponse(BaseModel):
    results: List[VideoClassificationResult]