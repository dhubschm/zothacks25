from fastapi import FastAPI, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List
from typing import Annotated

import json
import os

app = FastAPI()

class User(BaseModel):
    Email: str = None
    Username: str = None

app.mount("/static", StaticFiles(directory="../frontend"), name="static")

class Driver(BaseModel):
    UserInfo: User = None #Inherits User information (Email and Username)
    Cartype: str = None

class Event(BaseModel):
    Car_description: str = None
    #Host: Driver = None #Inherits Driver information (Userinfo and Cartype)
    Time: str = None
    Location: str = None
    Capacity: int = None #change to available seating and decrement it? 
    Attendees: List[User] = []

# Host=Driver(UserInfo=User(Username="foo",Email="bar"),)
users = [User(Username="foo",Email="bar")]
events_list = [
    Event(Car_description='Truck', Time='12:00PM',Location='UCI',Capacity=5,Attendees=[User(Username='Swagman', Email='swagman@uci.edu')]),
    Event(Car_description='Prius', Time='9:00AM',Location='Irvine, CA',Capacity=5,Attendees=[User(Username='Kaladin Stormblessed', Email='None')]),
    Event(Car_description='Bus', Time='1:00PM',Location='Universal Studios',Capacity=40,Attendees=[User(Username='Chancy', Email='boo@uci.edu')]),
    
]

#Creates a User class and adds it to a list of users
@app.post("/users/create/")
def create_user(username: Annotated[str, Form()], email: Annotated[str, Form()],):
    new_user = User(Username = username, Email = email)
    users.append(new_user)
    return {username: email}

#Creates an Event class and adds it to a list of events
@app.post("/event/makeevent/", response_class=RedirectResponse)
async def create_event(car_description: Annotated[str, Form()], destination: Annotated[str, Form()], capacity: Annotated[int, Form()], time: Annotated[str, Form()],):
    new_event = Event(Car_description = car_description, Location = destination, Capacity = capacity, Time = time)
    events_list.append(new_event)
    redirect_url = f"/static/index.html" ##?#eventcreator&eventname={eventname}&destination={destination}&capacity={capacity}&time={time}"
    return RedirectResponse(url=redirect_url, status_code=303)

#Adds a User class to a list of attendees in an Event class
@app.post("/events/join/{event_id}", response_model=Event)
def join_event(event_id: int, attendee: User):  
    event = events_list[event_id]

    if event.Capacity > 0:
        event.Attendees.append(attendee)
        event.Capacity -= 1
        return event
    else:
        raise HTTPException(status_code=503, detail=f"Event capacity for {event_id} is full")
    
#Retrieves a particular event in a list of events
@app.get("/events/viewevent/{event_id}", response_model=Event)
def get_event(event_id: int) -> Event:
    if event_id < len(events_list):
        event = events_list[event_id]
        return event
    else:
        raise HTTPException(status_code=404, detail=f"Event {event_id} not found")
    
@app.get("/events/", response_model=list)
def get_top_event():
    events = []
    for event in events_list[:9]:
        events.append(
            event.model_dump(mode='json', warnings=False)
        )
    return events

@app.get("/")
async def read_index():
    return FileResponse("../frontend/index.html")
