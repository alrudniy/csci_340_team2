from fastapi.testclient import TestClient

# Test the user registration endpoint - POST /api/v1/auth/register
def test_register(client: TestClient):
    data = {
        "email": "drew@gmail.com",
        "password": "Password1!",
        "username": "drew",
        "phone_number": "07085130123",
        "bio": "President of this woebegone Nation",
    }
    response = client.post("/api/v1/auth/register", json=data)
    assert response.status_code == 200, response.text
    response_data = response.json()
    user_data = response_data["data"]
    assert user_data["email"] == "drew@gmail.com"
    assert "id" in user_data



