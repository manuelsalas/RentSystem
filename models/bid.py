import sqlalchemy as sqlalchemy
from db import metadata
from models.enum import BidState

bid = sqlalchemy.Table(
    "bids",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("quantity", sqlalchemy.Integer),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("status", sqlalchemy.Enum(BidState), nullable=False, server_default=BidState.pending.name),
    sqlalchemy.Column("object_to_rent_id", sqlalchemy.ForeignKey("objects_to_rent.id"), nullable=False),
    sqlalchemy.Column("renter_id", sqlalchemy.ForeignKey("renters.id"), nullable=False),
)