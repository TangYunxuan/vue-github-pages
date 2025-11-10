from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db

from crud import user as crud
from schemas.user import UserCreate, UserUpdate, UserOut

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return user.list_users(db)

@router.get("/{item_id}")
def get_one(item_id: int, db: Session = Depends(get_db)):
    result = user.get_user(db, item_id)
    if not result: raise HTTPException(status_code=404, detail="Not found")
    return result

@router.post("/")
def create(item: UserCreate, db: Session = Depends(get_db)):
    return user.create_user(db, item)

@router.put("/{item_id}")
def update(item_id: int, item: UserUpdate, db: Session = Depends(get_db)):
    return user.update_user(db, item_id, item)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return user.delete_user(db, item_id)