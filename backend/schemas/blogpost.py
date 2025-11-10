# backend/schemas/blogpost.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BlogPostBase(BaseModel):
    title: str
    slug: str
    summary: Optional[str] = None
    content: Optional[str] = None

class BlogPostCreate(BlogPostBase):
    pass

class BlogPostUpdate(BaseModel):
    title: Optional[str] = None
    slug: Optional[str] = None
    summary: Optional[str] = None
    content: Optional[str] = None

class BlogPostOut(BlogPostBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        # v2 正式键；同时留 orm_mode 兼容 v1，无害
        from_attributes = True
        orm_mode = True