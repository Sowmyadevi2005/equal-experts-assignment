# Import required modules
from unittest.mock import patch, Mock
from src.app import app
import requests,pytest

# Fixture to initialize Flask test client
@pytest.fixture
def client():
    app.testing=True
    with app.test_client() as client:
        yield client

# Test case: Valid GitHub username should return 200 OK 
def test_gits_valid_user(client):
    response=client.get('/octocat')
    assert response.status_code == 200


# Test case: Valid GitHub username should return 200 OK but responsee is empty string
def test_gits_valid_user(client):
    response=client.get('/sowmya205')
    assert response.status_code == 200
    assert response.json["message"] == "No public gists exist for this user."

# est case: Nonexistent GitHub user should return 404
def test_404_user(client):
    response = client.get('/nonexistentuser123456')
    assert response.status_code == 404

# Test case: Unexpected error (e.g., 500 Internal Server Error) from GitHub
def test_unexpected_error_handling():
    with patch("src.app.requests.get") as mock_get:
        # Simulate GitHub returning status code 500
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        client = app.test_client()
        response = client.get("/octocat")

        assert response.status_code == 500
        assert response.json["error"] == "Unexpected error from GitHub (status code: 500)"