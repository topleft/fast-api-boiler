import uuid
import uvicorn

from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.src.repositories.db_repository import PsqlDbRepository
from app.src.repositories.items_repository import ItemsRepository
from app.src.data.models.items import Item, CreateItem


router = APIRouter()


def get_db():
    try:
        db_repository = PsqlDbRepository()
        yield db_repository.session
    finally:
        db_repository.close()


@router.get("/items/{id}", response_model=Item)
def get_single_item(id: uuid.UUID, db: Session = Depends(get_db)):
    item = ItemsRepository(db).get_one(id)
    return item


@router.get("/items", response_model=List[Item])
def get_items(*, db: Session = Depends(get_db)):
    items = ItemsRepository(db).get_all()
    return items


@router.post("/items", response_model=Item)
def create_item(*, db: Session = Depends(get_db), item_data: CreateItem):
    item = ItemsRepository(db).add(item_data)
    return item


