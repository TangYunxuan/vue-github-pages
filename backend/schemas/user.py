# backend/schemas/user.py
from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    avatar_url: Optional[str] = None
    bio: Optional[str] = None

class UserCreate(UserBase):
    password: str  # 若你不在创建时设置密码，可移除

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    avatar_url: Optional[str] = None
    bio: Optional[str] = None
    password: Optional[str] = None   # 如果支持修改密码，保留；否则删除

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True