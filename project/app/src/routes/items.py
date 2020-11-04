import uuid

from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.src.repositories.db_repository import PsqlDbRepository
from app.src.repositories.items_repository import ItemsRepository
from app.src.data.models.items import ItemSchema, ItemSchema__Create


router = APIRouter()


def get_db():
    try:
        db_repository = PsqlDbRepository()
        yield db_repository.session
    finally:
        db_repository.close()


@router.get("/items/{id}", response_model=ItemSchema)
def get_single_item(id: uuid.UUID, db: Session = Depends(get_db)):
    item = ItemsRepository(db).get_one(id)
    return item


@router.get("/items", response_model=List[ItemSchema])
def get_items(*, db: Session = Depends(get_db)):
    items = ItemsRepository(db).get_all()
    return items


@router.post("/items", response_model=ItemSchema)
def create_item(*, db: Session = Depends(get_db), item_data: ItemSchema__Create):
    item = ItemsRepository(db).add(item_data)
    return item
