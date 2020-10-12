import os
from logging import getLogger

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.data.models.base import Base

LOGGER = getLogger(__name__)


class PsqlDbRepository:
    def __init__(self):
        DB_URI = os.getenv("DB_URI", "db")
        DB_PORT = os.getenv("DB_PORT", "5432")
        DB_NAME = os.getenv("DB_NAME", "boiler")
        DB_USER = os.getenv("DB_USER", "boiler_user")
        DB_PASSWORD = os.getenv("DB_PASSWORD", "dev_admin")

        self.engine = create_engine(
            f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_URI}:{DB_PORT}/{DB_NAME}",
            connect_args={"options": "-c timezone=utc"}
        )
        self.session = sessionmaker(bind=self.engine)()
        self.metadata = Base.metadata
        self.metadata.bind = self.engine
        self.metadata.create_all()

    # Should always be called at the end of DB Transaction
    def close(self):
        self.session.close()

    def create(self, item):
        self.session.add(item)
        self.session.commit()
        return item

    def get_by_id(self, table, id):
        return self.session.query(table).filter(table.id == id).first()

    def update(self, table, id, item_updates):
        updated_item = self.session.query(table).\
            filter(table.id == id).first().\
            update(item_updates)
        self.session.commit()
        return updated_item

    def delete(self, table, id):
        no_of_deleted_items = self.session.query(table).\
            filter(table.id == id).\
            delete()
        self.session.commit()
        return no_of_deleted_items
