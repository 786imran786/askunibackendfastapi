from pydantic import BaseModel
from uuid import UUID

class VoteRequest(BaseModel):
    target_type: str  # question | answer
    target_id: UUID
    vote_type: str    # upvote | downvote
