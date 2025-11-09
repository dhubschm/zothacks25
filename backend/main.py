from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    Email: str = None
    Username: str = None

class Driver(BaseModel):
    UserInfo: User = None #Inherits User information (Email and Username)
    Cartype: str = None

class Event(BaseModel):
    EventName: str = None
    Host: Driver = None #Inherits Driver information (Userinfo and Cartype)
    Time: str = None
    Location: str = None
    Capacity: int = None #change to available seating and decrement it? 
    Attendees: List[User] = []

users = []
events_list = []

#Creates a User class and adds it to a list of users
@app.post("/users/create/", response_model=User)
def create_user(new_user: User):
    users.append(new_user)
    return new_user

#Creates an Event class and adds it to a list of events
@app.post("/event/postevent/", response_model=Event)
def create_event(new_event: Event):
    events_list.append(new_event)
    return new_event

#Adds a User class to a list of attendees in an Event class
@app.post("/events/join/{event_id}", response_model=Event)
def join_event(event_id: int, attendee: User):  #implement size handling? 
    event = events_list[event_id]

    if event.Capacity > 0:
        event.Attendees.append(attendee)
        event.Capacity -= 1
        return event
    else:
        raise HTTPException(status_code=503, detail=f"Event capacity for {event_id} is full")
    
#Retrieves a particular event in a list of events
@app.get("/events/viewevent/event_id}", response_model=Event)
def get_event(event_id: int) -> Event:
    if event_id < len(events_list):
        event = events_list[event_id]
        return event
    else:
        raise HTTPException(status_code=404, detail=f"Event {event_id} not found")