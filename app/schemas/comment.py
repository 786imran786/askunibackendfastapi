from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class CommentCreate(BaseModel):
    target_type: str   # question | answer
    target_id: UUID
    content: str

class CommentRead(BaseModel):
    id: UUID
    content: str
    created_at: datetime

    class Config:
        from_attributes = True
