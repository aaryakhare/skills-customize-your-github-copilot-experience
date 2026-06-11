from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

items = [
    {"id": 1, "name": "Notebook", "price": 3.5, "in_stock": True},
    {"id": 2, "name": "Pencil", "price": 0.99, "in_stock": True},
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/items")
def list_items(q: Optional[str] = None):
    if q:
        return [item for item in items if q.lower() in item["name"].lower()]
    return items

@app.post("/items")
def create_item(item: Item):
    new_id = max([item["id"] for item in items]) + 1
    new_item = item.dict()
    new_item["id"] = new_id
    items.append(new_item)
    return new_item
