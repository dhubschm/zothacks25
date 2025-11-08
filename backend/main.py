from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    Email: str = None
    Username: str = None

class Driver(BaseModel):
    UserInfo: User = None #Ingerits User information (Email and Username)
    Cartype: str = None

class Event(BaseModel):
    Host: Driver = None #Inherits Driver information (Userinfo and Cartype)
    Time: str = None
    Location: str = None
    Capacity: int = None
    Attendees: List[str] = []

users = []
events = []

@app.post("/users")
def create_user(new_user: User):
    users.append(new_user)
    return new_user

@app.post("/users/events")
def create_event(new_event: Event):
    events.append(new_event)
    return events

@app.post("/users/events/", response_model=Event)
def join_event(event: Event, attendee: User):
    event.Attendees.append(attendee)
    return event.Attendees

@app.get("/users/events/attendees", response_model=Event)
def list_attendees(event: Event, limit: int = 10):
    return event.Attendees[0:limit]

@app.get("/users/events", response_model=list[Event])
def list_events(limit: int = 10):
    return events[0:limit]


@app.get("/users/{event_id}", response_model=Event)
def get_event(event_id: int) -> Event:
    if event_id < len(events):
        return events[event_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {event_id} not found")