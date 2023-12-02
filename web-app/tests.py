""" 
Testing File For Flask Web Application
"""
from unittest.mock import MagicMock
import pytest
from app import app


# pylint: disable=pointless-string-statement
""" Testing Class """


# pylint: disable=missing-class-docstring
class Tests:
    @pytest.fixture
    def client(self):
        """
        Set up function for flask test client
        """
        app.config["TESTING"] = True
        with app.test_client() as client:
            yield client

    @pytest.fixture
    def mock_mongo_client(self, monkeypatch):
        """
        Set up fake mongo client
        """
        mock_client = MagicMock()
        monkeypatch.setattr("app.get_mongo_client", lambda uri: mock_client)
        return mock_client

    def test_index_route(self, client):
        """Test the index route."""
        response = client.get("/")
        assert response.status_code == 200

    def test_happy_route(self, client):
        """Test the happy route."""
        response = client.get("/happy_route")
        assert response.status_code == 200

    def test_sad_route(self, client):
        """Test the sad route."""
        response = client.get("/sad_route")
        assert response.status_code == 200

    def test_angry_route(self, client):
        """Test the angry route."""
        response = client.get("/angry_route")
        assert response.status_code == 200

    def test_surprised_route(self, client):
        """Test the surprised route."""
        response = client.get("/surprised_route")
        assert response.status_code == 200

    def test_fear_route(self, client):
        """Test the fear route."""
        response = client.get("/fear_route")
        assert response.status_code == 200
