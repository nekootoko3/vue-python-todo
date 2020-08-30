from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_read_item_empty():
    response = client.get("/api/v1/todos")
    assert response.status_code == 200

def test_create_todo():
    response = client.post(
        "/api/v1/todos",
        json={"title": "todo0"}
    )
    assert response.status_code == 201
