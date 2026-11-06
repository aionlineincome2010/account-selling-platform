from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    is_active: bool

    class Config:
        from_attributes = True

class AccountCreate(BaseModel):
    platform_type: str  # Gmail, Telegram, WhatsApp
    account_details: str
    price: float

class AccountResponse(BaseModel):
    id: int
    platform_type: str
    account_details: str
    price: float
    is_sold: bool

    class Config:
        from_attributes = True
