from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserOut
from database import SessionLocal

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserOut)
def create_item(item: UserCreate, db: Session = Depends(get_db)):
    db_item = User(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=list[UserOut])
def get_items(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/{item_id}", response_model=UserOut)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(User).filter(User.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="User not found")
    return item
