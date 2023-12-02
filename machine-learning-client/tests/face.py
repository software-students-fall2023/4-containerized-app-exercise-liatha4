""" 
Middle-man test module
"""
from deepface import DeepFace


def process_emotion(img):
    """
    Simple function for running the DeepFace Package
    Args:
        img (string): path to an image 

    Returns:
       dictionary: dictionary of information about emotions in image
    """
    result = DeepFace.analyze(img, actions=["emotion"])
    return result
