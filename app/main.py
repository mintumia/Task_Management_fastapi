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



@app.get("/")
async def root():
    return [{"message": "Hello World"}]


# @app.post("/users")
# async def create_user(request: Request, db: Session = Depends(get_db)):
#     data = await request.json()
#     db_user = models.User(data.get("name"), data.get("email"))
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

@app.post("/users")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    db_user = models.User(
        name=user.name,
        email=user.email
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/tests")
async def test(request: Request):
    data = await request.json()
    db_user = data.get("name"), data.get("email")
    return db_user




