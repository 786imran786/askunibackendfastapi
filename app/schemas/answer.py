from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class AnswerCreate(BaseModel):
    content: str

class AnswerRead(BaseModel):
    id: UUID
    content: str
    is_accepted: bool
    score: int
    created_at: datetime

    class Config:
        from_attributes = True
