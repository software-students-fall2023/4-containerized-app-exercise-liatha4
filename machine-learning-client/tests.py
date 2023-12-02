""" 
Testing File For ML Client using Flask Application
"""

import json
import pytest

# pylint: disable=import-error
import cv2
from app import app, process_emotion


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
