# schemas/blogpost.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class BlogPostBase(BaseModel):
    title: str
    content: str
    excerpt: str
    featured_image: Optional[str]
    tags: Optional[List[str]] = []
    published: bool = True

class BlogPostCreate(BlogPostBase):
    pass

class BlogPostRead(BlogPostBase):
    id: int
    created_date: datetime

    class Config:
        orm_mode = True