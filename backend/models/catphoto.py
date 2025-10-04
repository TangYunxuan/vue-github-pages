from sqlalchemy import Column, Integer, String
from database import Base

class Catphoto(Base):
    __tablename__ = "catphotos"

    id = Column(Integer, primary_key=True, index=True)
    caption = Column(String, nullable=False)
    image_url = Column(String, nullable=False)
    created_date = Column(String, nullable=True)
