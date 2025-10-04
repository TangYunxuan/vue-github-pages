from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.catphoto import Catphoto
from schemas.catphoto import CatphotoCreate, CatphotoOut
from database import SessionLocal

router = APIRouter(prefix="/catphotos", tags=["Catphotos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CatphotoOut)
def create_item(item: CatphotoCreate, db: Session = Depends(get_db)):
    db_item = Catphoto(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=list[CatphotoOut])
def get_items(db: Session = Depends(get_db)):
    return db.query(Catphoto).all()

@router.get("/{item_id}", response_model=CatphotoOut)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Catphoto).filter(Catphoto.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Catphoto not found")
    return item
