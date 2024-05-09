from fastapi import FastAPI
from fastapi import Path
from fastapi import Body

from typing import Annotated

from models.item import Item
from models.offer import Offer
from models.image import Image

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

# Declare a list with a type parameter
"""
@app.put("/items/{id}")
async def update_item(
  id: Annotated[int, Path()],
  item: Annotated[Item, Body()]
):
  response = {"id": id, "item": item}
  return response
"""

# Set types
"""
@app.put("/items/{id}")
async def update_item(
  id: Annotated[int, Path()],
  item: Annotated[Item, Body()]
):
  response = {"id": id, "item": item}
  return response
"""

# Define a submodel
"""
@app.put("/items/{id}")
async def update_item(
  id: Annotated[int, Path()],
  item: Annotated[Item, Body()]
):
  response = {"id": id, "item": item}
  return response
"""

# Special types and validation
"""
@app.put("/items/{id}")
async def update_item(
  id: Annotated[int, Path()],
  item: Annotated[Item, Body()]
):
  response = {"id": id, "item": item}
  return response
"""

# Attributes with lists of submodels
@app.put("/items/{id}")
async def update_item(
  id: Annotated[int, Path()],
  item: Annotated[Item, Body()]
):
  response = {"id": id, "item": item}
  return response

# Deeply nested models
@app.post("/offers")
async def create_offer(offer: Annotated[Offer, Body(embed = True)]):
  return offer

# Bodies of pure lists
@app.post("/images/bulk")
async def create_images(images: list[Image]):
  return images

# Bodies of arbitrary dicts
@app.post("/weights/bukl")
def create_weights(weights: dict[int, float]):
  return weights
