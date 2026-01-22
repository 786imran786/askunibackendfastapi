from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base

class UserMedia(Base):
    __tablename__ = "user_media"

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True
    )

    profile_picture = Column(String, nullable=True)
    avatar = Column(String, nullable=True)
