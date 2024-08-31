from fastapi import FastAPI

from app import user_router

app = FastAPI()
app.include_router(user_router.router, prefix="/users")
