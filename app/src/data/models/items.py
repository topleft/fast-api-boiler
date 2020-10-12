import datetime
import uuid

from pydantic import BaseModel

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import (
    Column,
    DateTime,
    String
)

from data.models.base import Base


class ItemORM(Base):
    __tablename__ = "items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), nullable=True)
    name = Column(String, nullable=False)

    def __init__(self, **kwargs):
        super(ItemORM, self).__init__(**kwargs)


class Item(BaseModel):
    id: uuid.UUID
    created_at: datetime.date
    updated_at: datetime.date
    name: str
