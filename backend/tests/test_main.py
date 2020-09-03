from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.app import crud, schemas

def test_read_item_empty(client: TestClient):
    response = client.get("/api/v1/todos")
    assert response.status_code == 200
    assert response.json() == []

def test_read_items(client: TestClient, db: Session):
    title = "todo0"
    model_todo = crud.create_todo(db, schemas.TodoCreate(title=title))
    response = client.get("/api/v1/todos")
    assert response.status_code == 200
    assert len(response.json()) == 1
    res_todo = response.json()[0]
    assert res_todo["id"] == model_todo.id
    assert res_todo["title"] == model_todo.title

def test_create_todo(client: TestClient):
    response = client.post(
        "/api/v1/todos",
        json={"title": "todo0"}
    )
    assert response.status_code == 201

def test_update_todo(client: TestClient, db: Session):
    title = "todo0"
    model_todo = crud.create_todo(db, schemas.TodoCreate(title=title))
    title_updated = "updated_todo"
    response = client.put(f"/api/v1/todos/{model_todo.id}", json={"title": title_updated})
    assert response.status_code == 200
    res_todo = response.json()
    assert res_todo["title"] == title_updated
