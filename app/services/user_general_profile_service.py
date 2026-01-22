from sqlalchemy.orm import Session

from app.models.user_general_profile import UserGeneralProfile
from app.models.user import User
from app.schemas.user_general_profile import UserGeneralProfileCreate

def create_or_update_general_profile(
    db: Session,
    user: User,
    data: UserGeneralProfileCreate
):
    profile = db.query(UserGeneralProfile).filter(
        UserGeneralProfile.user_id == user.id
    ).first()

    payload = {
        "short_bio": data.short_bio,
        "skills": ",".join(data.skills),
        "interests": ",".join(data.interests),
        "linkedin": data.linkedin,
        "github": data.github,
        "portfolio": data.portfolio
    }

    if profile:
        for key, value in payload.items():
            setattr(profile, key, value)
    else:
        profile = UserGeneralProfile(
            user_id=user.id,
            **payload
        )
        db.add(profile)

    db.commit()
    db.refresh(profile)
    return profile
