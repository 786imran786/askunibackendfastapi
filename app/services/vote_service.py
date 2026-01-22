from sqlalchemy.orm import Session
from app.models.vote import Vote
from app.models.user import User
from sqlalchemy import func, case

def vote_toggle(
    db: Session,
    user: User,
    target_type: str,
    target_id,
    vote_type: str
):
    existing = (
        db.query(Vote)
        .filter(
            Vote.user_id == user.id,
            Vote.target_type == target_type,
            Vote.target_id == target_id
        )
        .first()
    )

    # Same vote again → remove
    if existing and existing.vote_type == vote_type:
        db.delete(existing)
        db.commit()
        return "removed"

    # Change vote
    if existing:
        existing.vote_type = vote_type
        db.commit()
        return "updated"

    # New vote
    vote = Vote(
        user_id=user.id,
        target_type=target_type,
        target_id=target_id,
        vote_type=vote_type
    )
    db.add(vote)
    db.commit()
    return "added"


def get_vote_score(
    db: Session,
    target_type: str,
    target_id
) -> int:
    result = (
        db.query(
            func.coalesce(
                func.sum(
                    case(
                        (Vote.vote_type == "upvote", 1),
                        (Vote.vote_type == "downvote", -1),
                        else_=0
                    )
                ),
                0
            )
        )
        .filter(
            Vote.target_type == target_type,
            Vote.target_id == target_id
        )
        .scalar()
    )
    return result