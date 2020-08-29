from sqlalchemy.orm import Session

from . import models, schemas

def get_todos(db: Session):
    return db.query(models.Item).all()

def create_todo(db: Session, item: schemas.TodoCreate):
    db_todo = models.Todo(**item.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
