from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename__ = "players"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    username = Column(String(50))
    balance = Column(Integer, default=100)
    health = Column(Integer, default=100)
    is_admin = Column(Boolean, default=False))
