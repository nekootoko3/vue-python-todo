from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .crud import *
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/todos", response_model=List[schemas.Todo], status_code=200)
def read_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)


@app.post("/api/v1/todos", response_model=schemas.Todo,  status_code=201)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)

@app.delete("/api/v1/todos/{todo_id}", status_code=200)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    return crud.delete_todo(db=db, todo_id=todo_id)
