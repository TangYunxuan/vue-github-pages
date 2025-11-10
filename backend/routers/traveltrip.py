from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from crud import traveltrip as crud
from schemas.traveltrip import TravelTripCreate, TravelTripUpdate, TravelTripOut

router = APIRouter(prefix="/api/traveltrips", tags=["TravelTrips"])

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return traveltrip.list_traveltrips(db)

@router.get("/{item_id}")
def get_one(item_id: int, db: Session = Depends(get_db)):
    result = traveltrip.get_traveltrip(db, item_id)
    if not result: raise HTTPException(status_code=404, detail="Not found")
    return result

@router.post("/")
def create(item: TravelTripCreate, db: Session = Depends(get_db)):
    return traveltrip.create_traveltrip(db, item)

@router.put("/{item_id}")
def update(item_id: int, item: TravelTripUpdate, db: Session = Depends(get_db)):
    return traveltrip.update_traveltrip(db, item_id, item)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return traveltrip.delete_traveltrip(db, item_id)