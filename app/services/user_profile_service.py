from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.user_profile import UserProfile
from app.models.user import User
from app.schemas.user_profile import UserProfileCreate

def create_or_update_profile(
    db: Session,
    user: User,
    profile_in: UserProfileCreate
):
    profile = db.query(UserProfile).filter(
        UserProfile.user_id == user.id
    ).first()

    if profile:
        for key, value in profile_in.dict().items():
            setattr(profile, key, value)
    else:
        profile = UserProfile(
            user_id=user.id,
            **profile_in.dict()
        )
        db.add(profile)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("Username already taken")

    db.refresh(profile)
    return profile
