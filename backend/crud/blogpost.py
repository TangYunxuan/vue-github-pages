from sqlalchemy.orm import Session
from sqlalchemy import select
from models.blogpost import BlogPost
from database import get_db
from fastapi import Depends, HTTPException

def list_blogposts(db: Session):
    return db.exec(select(BlogPost)).all()

def get_blogpost(id: int, db: Session):
    blogpost = db.get(BlogPost, id)
    if not blogpost:
        raise HTTPException(status_code=404, detail="BlogPost not found")
    return blogpost

def create_blogpost(blogpost: BlogPost, db: Session):
    db.add(blogpost)
    db.commit()
    db.refresh(blogpost)
    return blogpost

def update_blogpost(id: int, updated: BlogPost, db: Session):
    blogpost = db.get(BlogPost, id)
    if not blogpost:
        raise HTTPException(status_code=404, detail="Not found")
    blogpost.title = updated.title
    blogpost.content = updated.content
    db.commit()
    db.refresh(blogpost)
    return blogpost

def delete_blogpost(id: int, db: Session):
    blogpost = db.get(BlogPost, id)
    if not blogpost:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(blogpost)
    db.commit()
    return {"message": "Deleted"}