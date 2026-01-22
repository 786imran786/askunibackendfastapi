from sqlalchemy.orm import Session

from app.models.user_profile import UserProfile
from app.models.user_designation import UserDesignation
from app.models.user_general_profile import UserGeneralProfile
from app.models.user_media import UserMedia
from app.models.user import User

def get_onboarding_status(db: Session, user: User):
    personal_info = db.query(UserProfile).filter(
        UserProfile.user_id == user.id
    ).first()

    designation = db.query(UserDesignation).filter(
        UserDesignation.user_id == user.id
    ).first()

    general_profile = db.query(UserGeneralProfile).filter(
        UserGeneralProfile.user_id == user.id
    ).first()

    media = db.query(UserMedia).filter(
        UserMedia.user_id == user.id
    ).first()

    steps = {
        "personal_info": bool(personal_info),
        "designation": bool(designation),
        "general_profile": bool(general_profile),
        "profile_media": bool(media),
    }

    all_completed = all(steps.values())

    return {
        "steps": steps,
        "completed": all_completed
    }
