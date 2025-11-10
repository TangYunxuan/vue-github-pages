from models.comment import Comment
from sqlalchemy.orm import Session
from schemas.comment import CommentCreate, CommentUpdate

def list_comments(db: Session):
    return db.query(Comment).all()

def get_comment(db: Session, item_id: int):
    return db.query(Comment).filter(Comment.id == item_id).first()

def create_comment(db: Session, item: CommentCreate):
    db_item = Comment(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_comment(db: Session, item_id: int, item: CommentUpdate):
    db_item = db.query(Comment).filter(Comment.id == item_id).first()
    if db_item:
        db_item.author = item.author
        db_item.text = item.text
        db_item.post_id = item.post_id
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_comment(db: Session, item_id: int):
    db_item = db.query(Comment).filter(Comment.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item