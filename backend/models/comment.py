from sqlalchemy import Column, Integer, String
from database import Base

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    author = Column(String, nullable=False)
    text = Column(String, nullable=False)
    post_id = Column(Integer, nullable=False)
    created_date = Column(String, nullable=True)
