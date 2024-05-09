from pydantic import BaseModel

from .image import Image

class Item(BaseModel):
  name: str
  description: str | None = None
  price: float
  tax: float | None = None
  images: list[Image] | None = None
  tags: set[str] = ()
