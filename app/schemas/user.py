from msgspec import Struct
from typing import Optional
from datetime import datetime

class UserCreate(Struct):
    name: str
    surname: str
    password: str

class UserUpdate(Struct):
    name: str
    surname: str
    password: Optional[str] = None

class UserResponse(Struct):
    id: int
    name: str
    surname: str
    created_at: datetime
    updated_at: datetime