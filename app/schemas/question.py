from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class QuestionCreate(BaseModel):
    title: str
    content: str

class QuestionRead(BaseModel):
    id: UUID
    title: str
    content: str
    views: int
    score: int
    created_at: datetime

    class Config:
        from_attributes = True
    
