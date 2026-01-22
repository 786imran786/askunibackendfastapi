from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.core.dependencies import get_current_user
from app.schemas.user_profile import UserProfileCreate
from app.services.user_profile_service import create_or_update_profile
from app.models.user import User
from app.schemas.user_designation import UserDesignationCreate
from app.services.user_designation_service import create_or_update_designation
from app.schemas.user_general_profile import UserGeneralProfileCreate
from app.services.user_general_profile_service import create_or_update_general_profile
from app.schemas.user_media import UserMediaCreate
from app.services.user_media_service import create_or_update_user_media
from app.services.onboarding_status_service import get_onboarding_status

router = APIRouter(prefix="/onboarding", tags=["Onboarding"])

@router.post("/personal-info")
def save_personal_info(
    profile_in: UserProfileCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        profile = create_or_update_profile(db, current_user, profile_in)
        return {"message": "Personal info saved", "profile_id": str(profile.user_id)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/designation")
def save_designation(
    data: UserDesignationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if data.designation_type not in ["student", "faculty", "alumni"]:
        raise HTTPException(status_code=400, detail="Invalid designation type")

    designation = create_or_update_designation(
        db,
        current_user,
        data
    )

    return {"message": "Designation saved"}

@router.post("/general-profile")
def save_general_profile(
    data: UserGeneralProfileCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    profile = create_or_update_general_profile(
        db,
        current_user,
        data
    )

    return {"message": "General profile saved"}

@router.post("/profile-media")
def save_profile_media(
    data: UserMediaCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    media = create_or_update_user_media(
        db,
        current_user,
        data
    )
    return {"message": "Profile media saved"}

@router.get("/status")
def onboarding_status(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_onboarding_status(db, current_user)
