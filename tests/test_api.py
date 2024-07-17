import json

def test_health(client):
    try:
        res = client.get("/health")
        assert res.status_code == 200, f"Expected status code 200, but got {res.status_code}"

        data = res.json()  # Assuming the response is JSON
        assert "status" in data, "Expected 'status' key in response data"

        # Add more assertions as needed to validate the content of the response
        # For example:
        # assert data["status"] == "healthy", "Expected status to be 'healthy'"

        print("Health check test passed successfully.")
    except Exception as e:
        print(f"Health check test failed: {e}")
        raise
