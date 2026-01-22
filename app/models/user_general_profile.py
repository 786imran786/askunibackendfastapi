from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base

class UserGeneralProfile(Base):
    __tablename__ = "user_general_profiles"

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True
    )

    short_bio = Column(String, nullable=False)

    # stored as comma-separated values (simple & fast)
    skills = Column(String, nullable=False)
    interests = Column(String, nullable=False)

    linkedin = Column(String, nullable=True)
    github = Column(String, nullable=True)
    portfolio = Column(String, nullable=True)
