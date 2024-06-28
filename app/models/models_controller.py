from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base

from models.model_base import BareBaseModel


class User(BareBaseModel):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Book(BareBaseModel):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    description = Column(String)
    price = Column(Float)
    in_stock = Column(Integer)
