# backend/routers/blogpost.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.blogpost import BlogPostCreate, BlogPostUpdate, BlogPostOut
from crud import blogpost as crud

router = APIRouter(prefix="/blogposts", tags=["blogposts"])

@router.post("/", response_model=BlogPostOut)
def create_post(item: BlogPostCreate, db: Session = Depends(get_db)):
    return crud.create_blogpost(db, item)  # 返回 ORM 对象没问题；FastAPI 会用 BlogPostOut 序列化

@router.get("/", response_model=list[BlogPostOut])
def list_posts(db: Session = Depends(get_db), skip: int = 0, limit: int = 20):
    return crud.get_blogposts(db, skip=skip, limit=limit)

@router.get("/{post_id}", response_model=BlogPostOut)
def get_post(post_id: int, db: Session = Depends(get_db)):
    obj = crud.get_blogpost(db, post_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.put("/{post_id}", response_model=BlogPostOut)
def update_post(post_id: int, item: BlogPostUpdate, db: Session = Depends(get_db)):
    obj = crud.update_blogpost(db, post_id, item)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.delete("/{post_id}", response_model=BlogPostOut)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_blogpost(db, post_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj