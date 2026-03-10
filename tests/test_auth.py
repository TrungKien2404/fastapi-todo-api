from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_success():

    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "test1@gmail.com",
            "password": "123456"
        }
    )

    assert response.status_code == 200


def test_register_validation_fail():

    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "invalid-email",
            "password": "123456"
        }
    )

    assert response.status_code == 422