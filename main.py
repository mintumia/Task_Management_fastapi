from fastapi import FastAPI
from pathlib import Path
from typing import List

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id":user_id}