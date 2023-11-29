# simple emotion read
import cv2 
from deepface import DeepFace 

def process_emotion(img):
    result = DeepFace.analyze(img,actions=['emotion']) 
    return result