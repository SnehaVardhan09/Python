from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI()


inventory={
    1: {
        "name": "TATA NEXON",
        "price": 1500000,
        "Category": "SUV"
    }
}

@app.get("/")  #endpoint
def home():
    return {"Data": "Testing, World!"}   

@app.get("/about")
def about():
    return {"Data": "About us!"}

@app.get("/get-item/{item_id}")  #endppoint with path parameter
def get_item(item_id:int):
    if item_id in inventory:
        return inventory[item_id]
    else:
        return {"Error": "Item not found"}
    
@app.get("/get-by-name")
def get_item(name: str): #query paramete
    for item in inventory:
        if inventory[item]["name"]==name:
            return inventory[item]
    return {"Error": "Item not found"}

