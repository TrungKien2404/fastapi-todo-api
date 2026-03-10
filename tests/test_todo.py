from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def get_token():

    client.post(
        "/api/v1/auth/register",
        json={
            "email": "todo@gmail.com",
            "password": "123456"
        }
    )

    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "todo@gmail.com",
            "password": "123456"
        }
    )

    return response.json()["access_token"]


def test_create_todo():

    token = get_token()

    response = client.post(
        "/api/v1/todos",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "title": "Learn FastAPI",
            "description": "Homework"
        }
    )

    assert response.status_code == 200


def test_auth_fail():

    response = client.post(
        "/api/v1/todos",
        json={
            "title": "Fail test"
        }
    )

    assert response.status_code == 200