from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.comment import CommentCreate, CommentRead
from app.services.comment_service import create_comment, get_comments
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/comments", tags=["Comments"])

@router.post(
    "",
    response_model=CommentRead,
    status_code=status.HTTP_201_CREATED
)
def add_comment(
    comment_in: CommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if comment_in.target_type not in ["question", "answer"]:
        raise HTTPException(status_code=400, detail="Invalid target type")

    return create_comment(db, current_user, comment_in)


@router.get(
    "",
    response_model=List[CommentRead]
)
def list_comments(
    target_type: str,
    target_id,
    db: Session = Depends(get_db)
):
    if target_type not in ["question", "answer"]:
        raise HTTPException(status_code=400, detail="Invalid target type")

    return get_comments(db, target_type, target_id)
