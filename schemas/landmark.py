from pydantic import BaseModel
from typing import List

class LandmarkItem(BaseModel) :
    nama: str
    desc: str
    fact: str


class LandmarkResponse(BaseModel):
    Landmark_prediction:LandmarkItem


