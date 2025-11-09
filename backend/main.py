from fastapi import FastAPI, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import List
from typing import Annotated


app = FastAPI()

#app.mount("/static", StaticFiles(directory="../frontend"), name="static")
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

class User(BaseModel):
    Email: str = None
    Username: str = None

#app.mount("/static", StaticFiles(directory="../frontend"), name="static")c
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

class Driver(BaseModel):
    UserInfo: User = None #Inherits User information (Email and Username)
    Cartype: str = None

class Event(BaseModel):
    EventName: str = None
    #Host: Driver = None #Inherits Driver information (Userinfo and Cartype)
    Time: str = None
    Location: str = None
    Capacity: int = None #change to available seating and decrement it? 
    Attendees: List[User] = []

users = []
events_list = []

#Creates a User class and adds it to a list of users
@app.post("/users/create/")
def create_user(username: Annotated[str, Form()], email: Annotated[str, Form()],):
    new_user = User(Username = username, Email = email)
    users.append(new_user)
    return {username: email}

#Creates an Event class and adds it to a list of events
@app.post("/event/makeevent/", response_class=RedirectResponse)
async def create_event(eventname: Annotated[str, Form()], destination: Annotated[str, Form()], capacity: Annotated[int, Form()], time: Annotated[str, Form()],):
    new_event = Event(EventName = eventname, Location = destination, Capacity = capacity, Time = time)
    events_list.append(new_event)
    redirect_url = f"/static/index.html" ##?#eventcreator&eventname={eventname}&destination={destination}&capacity={capacity}&time={time}"
    return RedirectResponse(url=redirect_url, status_code=303)
    #return RedirectResponse(url="http://127.0.0.1:8000/static/index.html?#eventcreator", status_code=303)

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