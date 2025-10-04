from sqlmodel import SQLModel, Field
from typing import Optional, List
from datetime import datetime

class BlogPost(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    excerpt: str
    featured_image: Optional[str] = None
    tags: Optional[str] = None  # 存为 JSON 字符串或以 , 分隔
    published: bool = True
    created_date: datetime = Field(default_factory=datetime.utcnow)