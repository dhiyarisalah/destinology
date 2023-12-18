from pydantic import BaseModel
from typing import List

class IteniaryItem(BaseModel):
    place_name: str
    price: int
    category: str
    rating: float
    day: int

class IteniaryResponse(BaseModel):
    itinerary: List[IteniaryItem]

class IteniaryRequest(BaseModel):
    city: str
    n_days: int
    max_budget: int
