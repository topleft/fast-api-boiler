from app.src.data.models.items import ItemORM, CreateItem
from sqlalchemy.orm import Session


class ItemsRepository():
    def __init__(self, db: Session):
        self.db = db

    def get_one(self, id: str):
        return self.db.query(ItemORM).filter(ItemORM.id == id)
        pass

    def get_all(self):
        return self.db.query(ItemORM).all()

    def add(self, item_data: CreateItem):
        item = ItemORM(name=item_data.name)
        self.db.add(item)
        self.db.commit()
        return item


