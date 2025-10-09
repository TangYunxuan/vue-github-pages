from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import traveltrip
from schemas import TraveltripCreate, TraveltripUpdate
from database import get_db

router = APIRouter(prefix="/api/traveltrips", tags=["Traveltrips"])

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return traveltrip.list_traveltrips(db)

@router.get("/{item_id}")
def get_one(item_id: int, db: Session = Depends(get_db)):
    result = traveltrip.get_traveltrip(db, item_id)
    if not result: raise HTTPException(status_code=404, detail="Not found")
    return result

@router.post("/")
def create(item: TraveltripCreate, db: Session = Depends(get_db)):
    return traveltrip.create_traveltrip(db, item)

@router.put("/{item_id}")
def update(item_id: int, item: TraveltripUpdate, db: Session = Depends(get_db)):
    return traveltrip.update_traveltrip(db, item_id, item)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return traveltrip.delete_traveltrip(db, item_id)