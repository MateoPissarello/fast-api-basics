from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(length=50), unique=True)
    password = Column(String(length=50))
    name = Column(String(length=50))
    last_name = Column(String(length=50))
    address = Column(String(length=255))
    phone_number = Column(String(length=20))
    email = Column(String(length=100), unique=True)
    created_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    state = Column(Boolean, default=False)
    sell = relationship("Sell", backref="users", cascade="delete,merge")


class Sell(Base):
    __tablename__ = "sell"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    sell = Column(Integer)
    sells_products = Column(Integer)
