from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_db
from models.blogpost import BlogPost
from crud.blogpost import (
    list_blogposts, get_blogpost, create_blogpost,
    update_blogpost, delete_blogpost
)

router = APIRouter(prefix="/api/blogposts", tags=["BlogPosts"])

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return list_blogposts(db)

@router.get("/{id}")
def get_one(id: int, db: Session = Depends(get_db)):
    return get_blogpost(id, db)

@router.post("/")
def create(blogpost: BlogPost, db: Session = Depends(get_db)):
    return create_blogpost(blogpost, db)

@router.put("/{id}")
def update(id: int, blogpost: BlogPost, db: Session = Depends(get_db)):
    return update_blogpost(id, blogpost, db)

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return delete_blogpost(id, db)