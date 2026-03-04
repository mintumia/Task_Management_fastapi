import time
from fastapi import FastAPI, HTTPException, status, responses, Request, Depends
from pydantic import BaseModel, HttpUrl
from pathlib import Path
from typing import List
import psycopg2
from psycopg2.extras import RealDictCursor

from app import create_app

from .db.database import engine, get_db
from . import models
from sqlalchemy.orm import Session
#import models.users as models
import app.schemas.user as schemas
import app.services.user_service as crud
#from database import engine, SessionLocal


app = create_app()









@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@app.get("/users", response_model=list[schemas.UserResponse])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}




@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)

    print(f"{request.method} {request.url.path} completed in {process_time} header: {request.headers['authorization']}")

    return response

@app.get("/")
async def root():
    return [{"message": "Hello World"}]





