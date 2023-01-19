from schemas.base import BaseModel
from models import Period
from typing import List


class ObjectIn(BaseModel):
    title: str
    description: str
    photo_url: str
    price: float
    price_period: Period

class ObjectInList(BaseModel):
    ObjectList: List[ObjectIn]
