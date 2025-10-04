from pydantic import BaseModel
from typing import Optional

class TraveltripBase(BaseModel):
    location: Optional[str] = None
    description: Optional[str] = None
    photo_url: Optional[str] = None
    date: Optional[str] = None

class TraveltripCreate(TraveltripBase):
    pass

class TraveltripOut(TraveltripBase):
    id: int

    class Config:
        orm_mode = True
