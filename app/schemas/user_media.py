from pydantic import BaseModel
from typing import Optional

class UserMediaCreate(BaseModel):
    profile_picture: Optional[str] = None
    avatar: Optional[str] = None
