# src/appointment_management.py

import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, field_validator
from src.user_management import User

class Appointment(BaseModel):
    user: User
    dates: Optional[List[str]] = Field(default_factory=list)
    
    @field_validator('dates', mode='before')
    def validate_dates(cls, dates):
        if dates is not None:
            validated_dates = []
            for date_str in dates:
                try:
                    datetime.datetime.strptime(date_str, "%Y-%m-%d")
                    validated_dates.append(date_str)
                except ValueError:
                    raise ValueError(f"Invalid date format for date: {date_str}. The date must be in the format yyyy-mm-dd.")
            return validated_dates
        return dates
