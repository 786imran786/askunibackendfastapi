from sqlalchemy.orm import Session
from app.models.question import Question
from app.schemas.question import QuestionCreate
from app.models.user import User

def create_question(
    db: Session,
    user: User,
    question_in: QuestionCreate
) -> Question:
    question = Question(
        user_id=user.id,
        title=question_in.title,
        content=question_in.content
    )
    db.add(question)
    db.commit()
    db.refresh(question)
    return question

def get_questions(
    db: Session,
    skip: int = 0,
    limit: int = 10
):
    return (
        db.query(Question)
        .order_by(Question.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

def get_question_by_id(db: Session, question_id):
    question = (
        db.query(Question)
        .filter(Question.id == question_id)
        .first()
    )
    if question:
        question.views += 1
        db.commit()
        db.refresh(question)
    return question
