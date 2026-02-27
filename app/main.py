import time
from fastapi import FastAPI, HTTPException, status, responses, Request
from pydantic import BaseModel, HttpUrl
from pathlib import Path
from typing import List
import psycopg2
from psycopg2.extras import RealDictCursor

from app import create_app


app = create_app()

while True:
    try:
        conn = psycopg2.connect(host="localhost", database="Task_Management_fastapi", user="postgres", password="1234",
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Connected to PostgreSQL")
        break

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        time.sleep(2)


class User(BaseModel):
    id: int
    name: str
    designation: str
    email: str
    password: str


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


# @app.get("/users")
# def users():
#     cursor.execute("SELECT * FROM users")
#     data = cursor.fetchall()
#     return {"data": data}


# @app.post("/users/create")
# def create_user(user: User):
#     cursor.execute("""INSERT INTO users (id, name, designation, email, password)
#                       VALUES (%s, %s, %s, %s, %s) RETURNING * """, (user.id, user.name, user.designation, user.email, user.password))
#
#
#
#     new_user = cursor.fetchone()
#     conn.commit()
#     return {"data": new_user}


