from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base

class UserDesignation(Base):
    __tablename__ = "user_designations"

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True
    )

    designation_type = Column(String, nullable=False)  
    # student | faculty | alumni

    # --- student fields ---
    registration_number = Column(String, nullable=True)
    program = Column(String, nullable=True)
    department = Column(String, nullable=True)
    current_year = Column(Integer, nullable=True)
    graduation_year = Column(Integer, nullable=True)
    college_email = Column(String, nullable=True)

    # --- faculty fields ---
    faculty_id = Column(String, nullable=True)
    post = Column(String, nullable=True)
    courses_taught = Column(String, nullable=True)
    office_location = Column(String, nullable=True)
    experience_years = Column(Integer, nullable=True)
    research = Column(String, nullable=True)

    # --- alumni fields ---
    job_title = Column(String, nullable=True)
    company_name = Column(String, nullable=True)
    linkedin = Column(String, nullable=True)
