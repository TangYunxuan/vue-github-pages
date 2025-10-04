from pydantic import BaseModel
from typing import Optional

class CommentBase(BaseModel):
    author: Optional[str] = None
    text: Optional[str] = None
    post_id: Optional[int] = None
    created_date: Optional[str] = None

class CommentCreate(CommentBase):
    pass

class CommentOut(CommentBase):
    id: int

    class Config:
        orm_mode = True
