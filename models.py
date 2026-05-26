from pydantic import BaseModel

class Item(BaseModel):
    city: str
    dish_name: str