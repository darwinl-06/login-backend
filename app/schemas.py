from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class ChangePassword(BaseModel):
    current_password: str
    new_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserResponse(UserBase):
    id: int
    is_admin: bool
    last_login: Optional[datetime] = None

    class Config:
        from_attributes = True 