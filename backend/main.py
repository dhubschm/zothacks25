from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    Email: str = None
    Username: str = None
    #is_done: bool = False

class Event(BaseModel):
    CarType: str = None
    Location: str = None
    Capacity: int = None


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


@app.get("/users/events", response_model=list[Event])
def list_events(limit: int = 10):
    return events[0:limit]


@app.get("/users/{event_id}", response_model=Event)
def get_event(event_id: int) -> Event:
    if event_id < len(events):
        return events[event_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {event_id} not found")