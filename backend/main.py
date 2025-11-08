from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str = None
    destination: str

items = []
#changed something
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{idem_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def save_item(item_id: int, item: Item):
    return {"item_name": item.destination, "item_id": item_id}