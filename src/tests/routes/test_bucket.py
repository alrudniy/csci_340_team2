from fastapi.testclient import TestClient

# Test the Bucket creation endpoint without auth - POST /api/v1/bucket
def test_create_bucket_auth_required(client: TestClient):
    response = client.post("/api/v1/bucket")
    assert response.status_code == 403  # Forbidden
    response_data = response.json()
    assert "detail" in response_data


