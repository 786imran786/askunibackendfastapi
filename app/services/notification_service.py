from sqlalchemy.orm import Session
from app.models.notification import Notification

def create_notification(
    db: Session,
    user_id,
    notif_type: str,
    reference_id=None
):
    notification = Notification(
        user_id=user_id,
        type=notif_type,
        reference_id=reference_id
    )
    db.add(notification)
    db.commit()

def mark_notification_read(db: Session, notification_id, user_id):
    notification = (
        db.query(Notification)
        .filter(
            Notification.id == notification_id,
            Notification.user_id == user_id
        )
        .first()
    )
    if not notification:
        return None

    notification.is_read = True
    db.commit()
    return notification


def mark_all_notifications_read(db: Session, user_id):
    db.query(Notification).filter(
        Notification.user_id == user_id,
        Notification.is_read == False
    ).update({"is_read": True})
    db.commit()