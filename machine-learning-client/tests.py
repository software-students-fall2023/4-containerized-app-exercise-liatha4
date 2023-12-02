""" 
Testing File For ML Client using Flask Application
"""
from unittest.mock import MagicMock
import json
import pytest
# pylint: disable=import-error
import cv2
from app import app, process_emotion



"""
Test class 
"""
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

    def test_process_emotion(self):
        """
        Test image processing
        """
        # pylint: disable=no-member
        img = cv2.imread("./test_face.png")
        result = process_emotion(img)
        assert isinstance(result, list), "Result is not a list"

    def test_process_emotion_invalid_input(self):
        """
        Test exception handling for image processing
        """
        with pytest.raises(AttributeError):
            process_emotion(None)

    def test_upload_image_no_data(self, client):
        """Test uploading image with no data."""
        response = client.post(
            "/image", data=json.dumps({}), content_type="application/json"
        )
        assert response.status_code == 400
