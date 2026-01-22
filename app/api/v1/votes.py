from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.vote import VoteRequest
from app.services.vote_service import vote_toggle
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/votes", tags=["Votes"])

@router.post("")
def vote(
    vote_in: VoteRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if vote_in.target_type not in ["question", "answer"]:
        raise HTTPException(status_code=400, detail="Invalid target type")

    if vote_in.vote_type not in ["upvote", "downvote"]:
        raise HTTPException(status_code=400, detail="Invalid vote type")

    result = vote_toggle(
        db,
        current_user,
        vote_in.target_type,
        vote_in.target_id,
        vote_in.vote_type
    )

    return {"status": result}
