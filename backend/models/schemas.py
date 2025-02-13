from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# DTOs (Data Transfer Objects)
class MessageDTO(BaseModel):
    text: str

class MessageResponse(BaseModel):
    text: str
    response: str

# Models
class Message(BaseModel):
    id: int
    text: str
    response: str
    created_at: datetime

    class Config:
        from_attributes = True
