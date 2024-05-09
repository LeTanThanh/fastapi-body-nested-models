from fastapi import FastAPI
from fastapi import Path
from fastapi import Body

from typing import Annotated

from models.item import Item

app = FastAPI()

# List fields
"""
@app.put("/items/{id}")
async def update_item(
  id: Annotated[int, Path()],
  item: Annotated[Item, Body()]
):
  response = {"id": id, "item": item}
  return response
"""
