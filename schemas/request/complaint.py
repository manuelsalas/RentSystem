from schemas.base import ComplaintBase
class ComplaintIn(ComplaintBase):
    encoded_photo: str
    extension: str