from sqlalchemy import Column, Integer, String
from database import Base

class Traveltrip(Base):
    __tablename__ = "traveltrips"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, nullable=False)
    description = Column(String, nullable=True)
    photo_url = Column(String, nullable=True)
    date = Column(String, nullable=True)
