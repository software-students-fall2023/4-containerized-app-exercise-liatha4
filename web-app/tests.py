import pytest
from unittest.mock import MagicMock
from app import app, get_mongo_client

@pytest.fixture
def client():
    # Set up Flask test client
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_mongo_client(monkeypatch):
    # Mock the MongoDB client
    mock_client = MagicMock()
    monkeypatch.setattr('app.get_mongo_client', lambda uri: mock_client)
    return mock_client

def test_index_route(client):
    """Test the index route."""
    response = client.get("/")
    assert response.status_code == 200

def test_happy_route(client):
    """Test the happy route."""
    response = client.get("/happy_route")
    assert response.status_code == 200

def test_sad_route(client):
    """Test the sad route."""
    response = client.get("/sad_route")
    assert response.status_code == 200

def test_angry_route(client):
    """Test the angry route."""
    response = client.get("/angry_route")
    assert response.status_code == 200

def test_surprised_route(client):
    """Test the surprised route."""
    response = client.get("/surprised_route")
    assert response.status_code == 200

def test_fear_route(client):
    """Test the fear route."""
    response = client.get("/fear_route")
    assert response.status_code == 200


