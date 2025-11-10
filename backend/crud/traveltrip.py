from models.traveltrip import Traveltrip
from sqlalchemy.orm import Session
from schemas.traveltrip import TravelTripCreate, TravelTripUpdate

def list_traveltrips(db: Session):
    return db.query(Traveltrip).all()

def get_traveltrip(db: Session, item_id: int):
    return db.query(Traveltrip).filter(Traveltrip.id == item_id).first()

def create_traveltrip(db: Session, item: TravelTripCreate):
    db_item = Traveltrip(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_traveltrip(db: Session, item_id: int, item: TravelTripUpdate):
    db_item = db.query(Traveltrip).filter(Traveltrip.id == item_id).first()
    if db_item:
        db_item.location = item.location
        db_item.description = item.description
        db_item.image_url = item.image_url
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_traveltrip(db: Session, item_id: int):
    db_item = db.query(Traveltrip).filter(Traveltrip.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item