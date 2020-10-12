from fastapi import FastAPI
import uvicorn

from app.repositories.db_repository import PsqlDbRepository
from app.data.models.items import ItemORM

app = FastAPI()

db = PsqlDbRepository()


@app.get("/")
async def hello():
    return {"body": "Hello World!"}


@app.get("/create-item")
def create_item():
    name = "Powza"
    item = ItemORM(name=name)
    db.session.add(item)
    db.session.commit()
    db.close()
    return {"name": name}

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000)
