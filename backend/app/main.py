from typing import Any, List
import os

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .crud import *
from . import crud, models, schemas
from .database import get_db

app = FastAPI()

origins = os.environ["CORS_URLS"].split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v1/todos", response_model=List[schemas.Todo], status_code=200)
def read_todos(db: Session = Depends(get_db)) -> Any:
    return crud.get_todos(db)


@app.post("/api/v1/todos", response_model=schemas.Todo,  status_code=201)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)) -> Any:
    return crud.create_todo(db=db, todo=todo)


@app.put("/api/v1/todos/{todo_id}", response_model=schemas.Todo,  status_code=200)
def create_todo(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)) -> Any:
    return crud.update_todo(db=db, todo_id=todo_id, todo=todo)


@app.delete("/api/v1/todos/{todo_id}", status_code=200)
def delete_todo(todo_id: int, db: Session = Depends(get_db)) -> Any:
    return crud.delete_todo(db=db, todo_id=todo_id)
