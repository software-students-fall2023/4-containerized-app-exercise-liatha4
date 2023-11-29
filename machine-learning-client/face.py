"""
This file provides a simple emotion read.
"""
from deepface import DeepFace

def process_emotion(img):
    """
    This function processes the emotion from the camera image and returns the emotion.
    :param arg1: image
    :return: returns the emotion
    :rtype: str
    """
    result = DeepFace.analyze(img,actions=['emotion'])
    return result
