from pydantic import BaseModel
from typing import Optional

class UserDesignationCreate(BaseModel):
    designation_type: str  # student | faculty | alumni

    # student
    registration_number: Optional[str]
    program: Optional[str]
    department: Optional[str]
    current_year: Optional[int]
    graduation_year: Optional[int]
    college_email: Optional[str]

    # faculty
    faculty_id: Optional[str]
    post: Optional[str]
    courses_taught: Optional[str]
    office_location: Optional[str]
    experience_years: Optional[int]
    research: Optional[str]

    # alumni
    job_title: Optional[str]
    company_name: Optional[str]
    linkedin: Optional[str]
