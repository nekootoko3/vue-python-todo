from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from . import models, schemas

def get_todo(db: Session, todo_id: int) -> models.Todo:
    try:
        return db.query(models.Todo).filter(models.Todo.id == todo_id).one()
    except NoResultFound:
        raise HTTPException(status_code=404, detail="not found")

def get_todos(db: Session) -> List[models.Todo]:
    return db.query(models.Todo).all()

def create_todo(db: Session, todo: schemas.TodoCreate) -> models.Todo:
    db_todo = models.Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int) -> None:
    model_todo = get_todo(db, todo_id)
    db.delete(model_todo)
    db.commit()
    return
