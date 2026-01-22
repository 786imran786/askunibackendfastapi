from pydantic import BaseModel
from typing import List, Optional

class UserGeneralProfileCreate(BaseModel):
    short_bio: str
    skills: List[str]
    interests: List[str]

    linkedin: Optional[str] = None
    github: Optional[str] = None
    portfolio: Optional[str] = None
