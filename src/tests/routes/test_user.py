from fastapi.testclient import TestClient

# Test the Get user endpoint without auth - GET /api/v1/user
def test_get_user_auth_required(client: TestClient):
    response = client.get("/api/v1/user")
    assert response.status_code == 403  # Forbidden
    response_data = response.json()
    assert "detail" in response_data

# Test the Get user endpoint with invalid token - GET /api/v1/user

def test_get_user_invalid_token(client: TestClient):
    invalid_auth_header = {"Authorization": "Bearer wrong.header"}
    response = client.get("/api/v1/user", headers=invalid_auth_header)
    assert response.status_code == 401, response.text
    response_data = response.json()
    assert "detail" in response_data