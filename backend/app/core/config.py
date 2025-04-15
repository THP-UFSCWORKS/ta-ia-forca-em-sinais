from fastapi import FastAPI
from app.api import ping

def create_app():
    app = FastAPI()
    app.include_router(ping.router)
    return app