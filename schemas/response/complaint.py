from datetime import datetime

from models import State
from schemas.base import ComplaintBase


class ComplaintOut(ComplaintBase):
    id: int
    photo_url: str
    created_at: datetime
    status: State

