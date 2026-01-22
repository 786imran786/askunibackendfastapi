from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.notification import NotificationRead
from app.core.dependencies import get_current_user
from app.models.user import User
from app.models.notification import Notification
from fastapi import HTTPException
from app.services.notification_service import (
    mark_notification_read,
    mark_all_notifications_read
)

router = APIRouter(prefix="/notifications", tags=["Notifications"])

@router.get("", response_model=List[NotificationRead])
def get_notifications(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return (
        db.query(Notification)
        .filter(Notification.user_id == current_user.id)
        .order_by(Notification.created_at.desc())
        .all()
    )

@router.post("/{notification_id}/read", response_model=NotificationRead)
def mark_read(
    notification_id,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    notification = mark_notification_read(
        db,
        notification_id,
        current_user.id
    )
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")

    return notification

@router.post("/read-all")
def mark_all_read(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    mark_all_notifications_read(db, current_user.id)
    return {"message": "All notifications marked as read"}
