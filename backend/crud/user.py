from models.user import User
from sqlalchemy.orm import Session
from schemas import userCreate, userUpdate

def list_users(db: Session):
    return db.query(User).all()

def get_user(db: Session, item_id: int):
    return db.query(User).filter(User.id == item_id).first()

def create_user(db: Session, item: userCreate):
    db_item = User(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_user(db: Session, item_id: int, item: userUpdate):
    db_item = db.query(User).filter(User.id == item_id).first()
    if db_item:
        db_item.username = item.username
        db_item.email = item.email
        db_item.bio = item.bio
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_user(db: Session, item_id: int):
    db_item = db.query(User).filter(User.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item