import sqlalchemy as sqlalchemy
from db import metadata
from models.enum import Period

# Data of object is denormalized because it could be changed by the owner
# the conditions when the renter made the bid and it was accepted must be preserved

renting = sqlalchemy.Table(
    "rentings",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("quantity", sqlalchemy.Integer),
    sqlalchemy.Column("title", sqlalchemy.String(120), nullable=False),
    sqlalchemy.Column("description", sqlalchemy.Text, nullable=False),
    sqlalchemy.Column("photo_url", sqlalchemy.String(200), nullable=False),
    sqlalchemy.Column("price", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("price_period", sqlalchemy.Enum(Period), nullable=False, server_default=Period.hour.name),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("bid_id", sqlalchemy.ForeignKey("renters.id"), nullable=False),
)