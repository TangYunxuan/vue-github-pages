from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.traveltrip import Traveltrip
from schemas.traveltrip import TraveltripCreate, TraveltripOut
from database import SessionLocal

router = APIRouter(prefix="/traveltrips", tags=["Traveltrips"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TraveltripOut)
def create_item(item: TraveltripCreate, db: Session = Depends(get_db)):
    db_item = Traveltrip(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=list[TraveltripOut])
def get_items(db: Session = Depends(get_db)):
    return db.query(Traveltrip).all()

@router.get("/{item_id}", response_model=TraveltripOut)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Traveltrip).filter(Traveltrip.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Traveltrip not found")
    return item
