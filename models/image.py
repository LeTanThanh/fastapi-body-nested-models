from pydantic import BaseModel
from pydantic import HttpUrl

class Image(BaseModel):
  url: HttpUrl
  name: str
