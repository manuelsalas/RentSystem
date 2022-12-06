from schemas.base import BaseModel
from models import Period


class OwnerObjectsIn(BaseModel):
    title: str
    description: str
    photo_url: str
    price: float
    price_period: Period
