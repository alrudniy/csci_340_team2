from fastapi.testclient import TestClient

# Test the Get user endpoint without auth - GET /api/v1/user
def test_get_user_auth_required(client: TestClient):
    response = client.get("/api/v1/user")
    assert response.status_code == 403  # Forbidden
    response_data = response.json()
    assert "detail" in response_data

