from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# User Model
class User(BaseModel):
    username: str
    password: str
    name: str
    last_name: str
    address: Optional[str]
    phone_number: str
    email: str
    created_at: datetime = datetime.now()


class ShowUser(BaseModel):
    username: str
    name: str
    email: str

    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    username: str = None
    password: str = None
    name: str = None
    last_name: str = None
    address: str = None
    phone_number: str = None
    email: str = None
