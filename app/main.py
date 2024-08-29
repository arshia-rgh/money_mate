from fastapi import FastAPI

from app.routers import user

app = FastAPI()

app.include_router(user.router, prefix="/user")
