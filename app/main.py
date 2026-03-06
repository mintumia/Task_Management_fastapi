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





