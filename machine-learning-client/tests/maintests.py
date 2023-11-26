import pytest
import json
import base64
import cv2
import numpy as np
from face import process_emotion
from main import app  # Import the Flask app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_process_emotion():
    img = cv2.imread("test_face.jpg")
    result = process_emotion(img)
    assert isinstance(result, list), "Result is not a list"

def test_process_emotion_invalid_input():
    with pytest.raises(Exception):
        process_emotion(None)
