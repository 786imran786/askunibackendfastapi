from sqlalchemy.orm import Session

from app.models.user_designation import UserDesignation
from app.models.user import User
from app.schemas.user_designation import UserDesignationCreate

def create_or_update_designation(
    db: Session,
    user: User,
    data: UserDesignationCreate
):
    designation = db.query(UserDesignation).filter(
        UserDesignation.user_id == user.id
    ).first()

    if designation:
        for key, value in data.dict().items():
            setattr(designation, key, value)
    else:
        designation = UserDesignation(
            user_id=user.id,
            **data.dict()
        )
        db.add(designation)

    db.commit()
    db.refresh(designation)
    return designation
