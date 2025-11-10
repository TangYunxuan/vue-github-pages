from pydantic import BaseModel
from typing import Optional

class CommentBase(BaseModel):
    author: Optional[str] = None
    text: Optional[str] = None
    post_id: Optional[int] = None
    created_date: Optional[str] = None

class CommentCreate(CommentBase):
    """用于创建评论"""
    pass

class CommentUpdate(BaseModel):
    """用于更新评论"""
    author: Optional[str] = None
    text: Optional[str] = None
    post_id: Optional[int] = None
    created_date: Optional[str] = None

class CommentOut(CommentBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True