from models.project import Project
from sqlalchemy.orm import Session
from schemas import projectCreate, projectUpdate

def list_projects(db: Session):
    return db.query(Project).all()

def get_project(db: Session, item_id: int):
    return db.query(Project).filter(Project.id == item_id).first()

def create_project(db: Session, item: projectCreate):
    db_item = Project(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_project(db: Session, item_id: int, item: projectUpdate):
    db_item = db.query(Project).filter(Project.id == item_id).first()
    if db_item:
        db_item.name = item.name
        db_item.description = item.description
        db_item.link = item.link
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_project(db: Session, item_id: int):
    db_item = db.query(Project).filter(Project.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item