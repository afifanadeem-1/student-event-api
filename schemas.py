from pydantic import BaseModel
from datetime import date


class EventCreate(BaseModel):
    title: str
    description: str
    date: date
    location: str
    organizer: str
    category: str


class EventResponse(EventCreate):
    id: int

    class Config:
        from_attributes = True
