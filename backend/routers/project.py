from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.project import Project
from schemas.project import ProjectCreate, ProjectOut
from database import SessionLocal

router = APIRouter(prefix="/projects", tags=["Projects"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProjectOut)
def create_item(item: ProjectCreate, db: Session = Depends(get_db)):
    db_item = Project(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=list[ProjectOut])
def get_items(db: Session = Depends(get_db)):
    return db.query(Project).all()

@router.get("/{item_id}", response_model=ProjectOut)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Project).filter(Project.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Project not found")
    return item
