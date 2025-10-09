from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import catphoto
from schemas import CatphotoCreate, CatphotoUpdate
from database import get_db

router = APIRouter(prefix="/api/catphotos", tags=["Catphotos"])

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return catphoto.list_catphotos(db)

@router.get("/{item_id}")
def get_one(item_id: int, db: Session = Depends(get_db)):
    result = catphoto.get_catphoto(db, item_id)
    if not result: raise HTTPException(status_code=404, detail="Not found")
    return result

@router.post("/")
def create(item: CatphotoCreate, db: Session = Depends(get_db)):
    return catphoto.create_catphoto(db, item)

@router.put("/{item_id}")
def update(item_id: int, item: CatphotoUpdate, db: Session = Depends(get_db)):
    return catphoto.update_catphoto(db, item_id, item)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return catphoto.delete_catphoto(db, item_id)