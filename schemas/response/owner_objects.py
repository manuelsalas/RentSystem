from pydantic import BaseModel
from datetime import datetime
from typing import List
from models import Period


class OwnerOut(BaseModel):
    id: int
    created_at: datetime
    user_id: int


class ObjectToRentOut(BaseModel):
    id: int
    title: str
    description: str
    photo_url: str
    price: float
    price_period: Period
    created_at: datetime
    owner_id: int

class ObjectToRentListOut(ObjectToRentOut):
    ObjToRentList: List[ObjectToRentOut]