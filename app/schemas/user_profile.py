from pydantic import BaseModel
from typing import Optional

class UserProfileCreate(BaseModel):
    full_name: str
    username: str
    phone: Optional[str] = None
    age: int
    gender: str  # Male / Female / Rather not to say
