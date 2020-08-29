from typing import List

from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str

class TodoCreate(TodoBase):
    title: str

class Todo(TodoBase):
    id: int
    title: str

    class Config:
        orm_mode = True
