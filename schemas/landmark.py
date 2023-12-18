from pydantic import BaseModel
from typing import List

class LandmarkResponse(BaseModel) :
    nama: str
    desc: str
    fact: str



