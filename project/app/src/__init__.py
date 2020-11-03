from typing import List
from fastapi import FastAPI, Depends
import uvicorn
from sqlalchemy.orm import Session
from app.src.repositories.db_repository import PsqlDbRepository
from app.src.data.models.items import Item, CreateItem, ItemORM

app = FastAPI()


def get_db():
    try:
        session = PsqlDbRepository().session
        yield session
    finally:
        session.close()


@app.get("/")
async def hello():
    return {"body": "Hello World!"}


@app.get("/items", response_model=List[Item])
def get_items(*, db: Session = Depends(get_db)):
    items = db.query(ItemORM).all()
    return items


@app.post("/items", response_model=Item)
def create_item(*, db: Session = Depends(get_db), item_data: CreateItem):
    item = ItemORM(name=item_data.name)
    db.add(item)
    db.commit()
    return item


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000)
