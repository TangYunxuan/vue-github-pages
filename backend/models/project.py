from sqlalchemy import Column, Integer, String
from database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    link = Column(String, nullable=True)
    tech_stack = Column(String, nullable=True)
