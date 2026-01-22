from sqlalchemy.orm import Session

from app.models.user_media import UserMedia
from app.models.user import User
from app.schemas.user_media import UserMediaCreate

def create_or_update_user_media(
    db: Session,
    user: User,
    data: UserMediaCreate
):
    media = db.query(UserMedia).filter(
        UserMedia.user_id == user.id
    ).first()

    if media:
        if data.profile_picture is not None:
            media.profile_picture = data.profile_picture
        if data.avatar is not None:
            media.avatar = data.avatar
    else:
        media = UserMedia(
            user_id=user.id,
            profile_picture=data.profile_picture,
            avatar=data.avatar
        )
        db.add(media)

    db.commit()
    db.refresh(media)
    return media
