from fastapi import FastAPI
from app.routers import users as users_router
import app.models.user as models
from .db.database import engine

def create_app() -> FastAPI:
    application = FastAPI()
    print("Creating FastAPI app")
    application.include_router(users_router.router)
    models.Base.metadata.create_all(bind=engine)
    return application
    #app.include_router(users_router)
    return app

