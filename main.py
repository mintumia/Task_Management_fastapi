import time

from fastapi import FastAPI
from pathlib import Path
from typing import List
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

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


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
def users():
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    return {"data":data}


# @app.get("/users/{user_id}")
# def read_user(user_id: int):
#     return {"user_id": user_id}
