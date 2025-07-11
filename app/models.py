from sqlalchemy import Column, Integer, String
from app.database import Base

class Person(Base):
    __tablename__ = "personnel"

    id = Column(Integer, primary_key=True, index=True)
    household_id = Column(String(50))
    address = Column(String(255))
    name = Column(String(50))
    relationship = Column(String(50))
    gender = Column(String(10))
    id_number = Column(String(18), unique=True)
    household_type = Column(String(50))
