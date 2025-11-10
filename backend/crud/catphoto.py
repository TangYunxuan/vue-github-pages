from models.catphoto import Catphoto
from sqlalchemy.orm import Session
from schemas.catphoto import CatPhotoCreate, CatPhotoUpdate

def list_catphotos(db: Session):
    return db.query(Catphoto).all()

def get_catphoto(db: Session, item_id: int):
    return db.query(Catphoto).filter(Catphoto.id == item_id).first()

def create_catphoto(db: Session, item: CatPhotoCreate):
    db_item = Catphoto(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_catphoto(db: Session, item_id: int, item: CatPhotoUpdate):
    db_item = db.query(Catphoto).filter(Catphoto.id == item_id).first()
    if db_item:
        db_item.caption = item.caption
        db_item.image_url = item.image_url
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_catphoto(db: Session, item_id: int):
    db_item = db.query(Catphoto).filter(Catphoto.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item