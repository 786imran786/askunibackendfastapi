from sqlalchemy.orm import Session
from app.models.answer import Answer
from app.schemas.answer import AnswerCreate
from app.models.user import User
from app.models.question import Question

def create_answer(
    db: Session,
    user: User,
    question_id,
    answer_in: AnswerCreate
) -> Answer:
    answer = Answer(
        user_id=user.id,
        question_id=question_id,
        content=answer_in.content
    )
    db.add(answer)
    db.commit()
    db.refresh(answer)
    return answer

def get_answers_by_question(db: Session, question_id):
    return (
        db.query(Answer)
        .filter(Answer.question_id == question_id)
        .order_by(Answer.is_accepted.desc(), Answer.created_at.asc())
        .all()
    )

def accept_answer(
    db: Session,
    current_user: User,
    answer_id
):
    answer = db.query(Answer).filter(Answer.id == answer_id).first()
    if not answer:
        return None, "Answer not found"

    question = db.query(Question).filter(Question.id == answer.question_id).first()
    if not question:
        return None, "Question not found"

    # Only question owner can accept
    if question.user_id != current_user.id:
        return None, "Not allowed"

    # Un-accept previous accepted answer (if any)
    db.query(Answer).filter(
        Answer.question_id == question.id,
        Answer.is_accepted == True
    ).update({"is_accepted": False})

    # Accept this answer
    answer.is_accepted = True
    db.commit()
    db.refresh(answer)

    return answer, None
