# backend/schemas/traveltrip.py
from typing import Optional
from pydantic import BaseModel
from datetime import date

class TravelTripBase(BaseModel):
    title: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    location: Optional[str] = None
    notes: Optional[str] = None

class TravelTripCreate(TravelTripBase):
    """用于创建"""
    pass

class TravelTripUpdate(BaseModel):
    """用于更新（全部可选）"""
    title: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    location: Optional[str] = None
    notes: Optional[str] = None

class TravelTripOut(TravelTripBase):
    id: int
    
    class Config:
        orm_mode = True
        from_attributes = True