from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from crud import comment as crud
from schemas.comment import CommentCreate, CommentUpdate, CommentOut

router = APIRouter(prefix="/api/comments", tags=["Comments"])

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return comment.list_comments(db)

@router.get("/{item_id}")
def get_one(item_id: int, db: Session = Depends(get_db)):
    result = comment.get_comment(db, item_id)
    if not result: raise HTTPException(status_code=404, detail="Not found")
    return result

@router.post("/")
def create(item: CommentCreate, db: Session = Depends(get_db)):
    return comment.create_comment(db, item)

@router.put("/{item_id}")
def update(item_id: int, item: CommentUpdate, db: Session = Depends(get_db)):
    return comment.update_comment(db, item_id, item)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return comment.delete_comment(db, item_id)