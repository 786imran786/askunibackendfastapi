from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.answer import AnswerCreate, AnswerRead
from app.services.answer_service import create_answer
from app.core.dependencies import get_current_user
from app.models.user import User
from app.models.question import Question
from typing import List
from app.services.answer_service import get_answers_by_question
from app.services.answer_service import accept_answer
from app.services.vote_service import get_vote_score
from fastapi import BackgroundTasks
from app.services.notification_service import create_notification
from app.models.question import Question

router = APIRouter(prefix="/answers", tags=["Answers"])

@router.post(
    "/question/{question_id}",
    response_model=AnswerRead,
    status_code=status.HTTP_201_CREATED
)
def add_answer(
    question_id,
    answer_in: AnswerCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    question = db.query(Question).filter(Question.id == question_id).first()
    # Notify question owner
    if question.user_id != current_user.id:
        background_tasks.add_task(
            create_notification,
            db,
            question.user_id,
        "answer",
        answer.id
    )

    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    return create_answer(db, current_user, question_id, answer_in)

@router.get(
    "/question/{question_id}",
    response_model=List[AnswerRead]
)
def list_answers(
    question_id,
    db: Session = Depends(get_db)
):
    answers = get_answers_by_question(db, question_id)

    return [
        {
            **a.__dict__,
            "score": get_vote_score(db, "answer", a.id)
        }
        for a in answers
    ]


@router.post("/{answer_id}/accept", response_model=AnswerRead)
def accept_answer_api(
    answer_id,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    answer, error = accept_answer(db, current_user, answer_id)
    if error == "Answer not found":
        raise HTTPException(status_code=404, detail=error)
    if error == "Question not found":
        raise HTTPException(status_code=404, detail=error)
    if error == "Not allowed":
        raise HTTPException(status_code=403, detail="Only question owner can accept")

    return answer
