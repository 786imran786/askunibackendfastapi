from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base

class UserProfile(Base):
    __tablename__ = "user_profiles"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)

    full_name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=True)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
