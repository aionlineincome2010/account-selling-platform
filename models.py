from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    platform_type = Column(String, index=True)  # Gmail, Telegram, WhatsApp
    account_details = Column(String)
    price = Column(Float)
    is_sold = Column(Boolean, default=False)
