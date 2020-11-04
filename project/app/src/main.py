import uvicorn

from fastapi import FastAPI

from app.src.routes import ping, items



app = FastAPI()

app.include_router(ping.router)
app.include_router(items.router, tags=["items"])


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000)
