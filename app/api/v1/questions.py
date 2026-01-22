from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.question import QuestionCreate, QuestionRead
from app.services.question_service import create_question
from app.core.dependencies import get_current_user
from app.models.user import User
from typing import List
from fastapi import HTTPException
from app.services.question_service import get_questions, get_question_by_id
from app.services.vote_service import get_vote_score

router = APIRouter(prefix="/questions", tags=["Questions"])

@router.post(
    "",
    response_model=QuestionRead,
    status_code=status.HTTP_201_CREATED
)
def create_question_api(
    question_in: QuestionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_question(db, current_user, question_in)

@router.get("", response_model=List[QuestionRead])
def list_questions(
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    skip = (page - 1) * limit
    questions = get_questions(db, skip=skip, limit=limit)

    return [
        {
            **q.__dict__,
            "score": get_vote_score(db, "question", q.id)
        }
        for q in questions
    ]
@router.get("/{question_id}", response_model=QuestionRead)
def get_question(question_id, db: Session = Depends(get_db)):
    question = get_question_by_id(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return {
    **question.__dict__,
    "score": get_vote_score(db, "question", question.id)
    }
