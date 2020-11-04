from typing import List
from fastapi import FastAPI, Depends
import uvicorn
from sqlalchemy.orm import Session
from app.src.repositories.db_repository import PsqlDbRepository
from app.src.repositories.items_repository import ItemsRepository
from app.src.data.models.items import Item, CreateItem, ItemORM


app = FastAPI()


def get_db():
    try:
        db_repository = PsqlDbRepository()
        yield db_repository.session
    finally:
        db_repository.close()


@app.get("/ping")
def ping():
    return {
        "status": "success",
        "message": "pong!"
    }


# @app.get("/items/{id}", response_model=List[Item])
# def get_items(id: int, db: Session = Depends(get_db)):
#     items = ItemRepository(db).get_all()
#     return items

@app.get("/items", response_model=List[Item])
def get_items(*, db: Session = Depends(get_db)):
    items = ItemsRepository(db).get_all()
    return items


@app.post("/items", response_model=Item)
def create_item(*, db: Session = Depends(get_db), item_data: CreateItem):
    item = ItemsRepository(db).add(item_data)
    return item


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000)
