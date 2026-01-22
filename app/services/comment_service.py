from sqlalchemy.orm import Session
from app.models.comment import Comment
from app.models.user import User
from app.schemas.comment import CommentCreate

def create_comment(
    db: Session,
    user: User,
    comment_in: CommentCreate
) -> Comment:
    comment = Comment(
        user_id=user.id,
        target_type=comment_in.target_type,
        target_id=comment_in.target_id,
        content=comment_in.content
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

def get_comments(
    db: Session,
    target_type: str,
    target_id
):
    return (
        db.query(Comment)
        .filter(
            Comment.target_type == target_type,
            Comment.target_id == target_id
        )
        .order_by(Comment.created_at.asc())
        .all()
    )
