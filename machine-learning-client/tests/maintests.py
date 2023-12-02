"""
    Tests for the ML Client
    Note pylint disables for cv2 package which are a known error
"""
import pytest
import cv2
from face import process_emotion
from main import app


@pytest.fixture
def client():
    """
    test that flask client can be accessed
    Yields:
        client: flask cleint
    """
    # pylint: disable=redefined-outer-name
    with app.test_client() as client:
        yield client


def test_process_emotion():
    """
    test to make sure that call to ML client returns a list
    """
    # pylint: disable=no-member
    img = cv2.imread("./test_face.png")
    result = process_emotion(img)
    assert isinstance(result, list), "Result is not a list"


def test_process_emotion_invalid_input():
    """
    test to make sure that ml client returns an exception if passed no arguments
    """
    with pytest.raises(Exception):
        process_emotion(None)
