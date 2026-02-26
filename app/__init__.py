from fastapi import FastAPI
from routers import __all__

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(__all__)
    return app