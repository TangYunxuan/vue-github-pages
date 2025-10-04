from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.comment import Comment
from schemas.comment import CommentCreate, CommentOut
from database import SessionLocal

router = APIRouter(prefix="/comments", tags=["Comments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CommentOut)
def create_item(item: CommentCreate, db: Session = Depends(get_db)):
    db_item = Comment(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=list[CommentOut])
def get_items(db: Session = Depends(get_db)):
    return db.query(Comment).all()

@router.get("/{item_id}", response_model=CommentOut)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Comment).filter(Comment.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Comment not found")
    return item
