from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, mapped_column
from database import Base

class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    email = mapped_column(String, unique=True, index=True)
    hashed_password = mapped_column(String)
    is_active = mapped_column(Boolean, default=True)
    
    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String, index=True)
    description = mapped_column(String, index=True)
    owner_id = mapped_column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
