from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List

app = FastAPI()

#app.mount("/static", StaticFiles(directory="../frontend"), name="static")
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

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
    Attendees: List[User] = []

users = []
events_list = []

#Creates a User class and adds it to a list of users
@app.post("/users", response_model=User)
def create_user(new_user: User):
    users.append(new_user)
    return new_user

#Creates an Event class and adds it to a list of events
@app.post("/users/events", response_model=Event)
def create_event(new_event: Event):
    events_list.append(new_event)
    return new_event

#Adds a User class to a list of attendees in an Event class
@app.post("/users/events/{event_id}", response_model=Event)
def join_event(event_id: int, attendee: User):
    event = events_list[event_id]
    event.Attendees.append(attendee)
    return event

#Displays the attendees (User classes) that exist in an Event class
@app.get("/users/events/attendees", response_model=list[User])
def list_attendees(event_id: int, limit: int = 10):
    event = events_list[event_id]
    return event.Attendees[0:limit]

#Lists up to 10 events in an event list
@app.get("/users/events", response_model=list[Event])
def list_events(limit: int = 10):
    return events_list[0:limit]

#Retrieves a particular event in a list of events
@app.get("/users/{event_id}", response_model=Event)
def get_event(event_id: int) -> Event:
    if event_id < len(events_list):
        event = events_list[event_id]
        return event
    else:
        raise HTTPException(status_code=404, detail=f"Item {event_id} not found")