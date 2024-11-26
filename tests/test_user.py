from fastapi import status


def test_create_user(client):
    response = client.post(
        "/api/v1/users",
        json={
            "username": "testuser",
            "password": "password123",
            "is_active": True
        }
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["username"] == "testuser"
    assert "id" in data


def test_get_user(client):
    # First create a user
    create_response = client.post(
        "/api/v1/users",
        json={
            "username": "testuser",
            "password": "password123",
            "is_active": True
        }
    )
    user_id = create_response.json()["id"]

    # Then get the user
    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["username"] == "testuser"
    assert data["id"] == user_id