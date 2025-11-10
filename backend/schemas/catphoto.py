# backend/schemas/catphoto.py
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, HttpUrl, Field

class CatPhotoBase(BaseModel):
    url: HttpUrl | str = Field(..., description="图片地址")
    caption: Optional[str] = ""
    taken_at: Optional[datetime] = None

class CatPhotoCreate(CatPhotoBase):
    pass

class CatPhotoUpdate(BaseModel):
    url: Optional[HttpUrl | str] = None
    caption: Optional[str] = None
    taken_at: Optional[datetime] = None

class CatPhotoOut(CatPhotoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # Pydantic v2; v1 仍兼容（同时留着 orm_mode 也行）
        orm_mode = True
        