# src/user_management.py

from typing import Optional
from pydantic import BaseModel, EmailStr, Field, field_validator
import re
import uuid

class UserInput(BaseModel):
    name: Optional[str] = None
    phone_no: Optional[str] = None
    email: Optional[EmailStr] = None

class User(UserInput):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    
    @field_validator('phone_no')
    def validate_phone_no(cls, phone_no):
        if phone_no:
            if not re.match(r"^(98|97)\d{8}$", phone_no):
                raise ValueError("Invalid Nepali phone number! It should start with 98 or 97 and have 10 digits.")
        return phone_no
