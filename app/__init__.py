from fastapi import FastAPI
from app.routers import users as users_router

def create_app() -> FastAPI:
    application = FastAPI()
    print("Creating FastAPI app")
    application.include_router(users_router.router)
    return application
    #app.include_router(users_router)
    return app

