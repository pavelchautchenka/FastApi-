from fastapi import FastAPI
from app.handlers.auth import router as auth_router
from app.handlers.events import  router as events_router
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


app.include_router(auth_router)
app.include_router(events_router)