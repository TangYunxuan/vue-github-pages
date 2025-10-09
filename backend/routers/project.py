from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import project
from schemas import ProjectCreate, ProjectUpdate
from database import get_db

router = APIRouter(prefix="/api/projects", tags=["Projects"])

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return project.list_projects(db)

@router.get("/{item_id}")
def get_one(item_id: int, db: Session = Depends(get_db)):
    result = project.get_project(db, item_id)
    if not result: raise HTTPException(status_code=404, detail="Not found")
    return result

@router.post("/")
def create(item: ProjectCreate, db: Session = Depends(get_db)):
    return project.create_project(db, item)

@router.put("/{item_id}")
def update(item_id: int, item: ProjectUpdate, db: Session = Depends(get_db)):
    return project.update_project(db, item_id, item)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return project.delete_project(db, item_id)