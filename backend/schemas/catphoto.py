from pydantic import BaseModel
from typing import Optional

class CatphotoBase(BaseModel):
    caption: Optional[str] = None
    image_url: Optional[str] = None
    created_date: Optional[str] = None

class CatphotoCreate(CatphotoBase):
    pass

class CatphotoOut(CatphotoBase):
    id: int

    class Config:
        orm_mode = True
