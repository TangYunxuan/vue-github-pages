from sqlmodel import Session, select
from models.blogpost import BlogPost
from database import engine

def list_blogposts():
    with Session(engine) as session:
        return session.exec(select(BlogPost).where(BlogPost.published == True).order_by(BlogPost.created_date.desc())).all()