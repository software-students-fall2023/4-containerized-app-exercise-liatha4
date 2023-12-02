"""
This file provides takes the emotion and uploads it to MongoDB,
processes the image data/emotions, and sends it to front-end as well.
"""
import os
import base64
from flask import Flask, request, jsonify
# pylint: disable=import-error
from cv2 import cv2
import numpy as np
import pymongo
from pymongo import MongoClient
from flask_cors import CORS
from dotenv import load_dotenv
from face import process_emotion


load_dotenv()

app = Flask(__name__)
CORS(app)


def get_mongo_client(uri):
    """Create and return a MongoDB client."""
    return MongoClient(uri)


mongo_uri = os.getenv("MONGO_URI")
client = get_mongo_client(mongo_uri)
db = client[os.getenv("MONGO_DBNAME")]
facedata = db.facedata


@app.route("/image", methods=["POST"])
def upload_image():
    """Route for parsing image received from webcam into expression data"""
    data = request.json
    if not data or "image" not in data:
        return "No image data", 400

    image_data = data["image"]
    encoded_data = image_data.split(",")[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    # pylint: disable=c-extension-no-member
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    emotion_result = process_emotion(img)

    try:
        document = {"output": emotion_result}
        facedata.insert_one(document)
        return jsonify(emotion_result), 200
    except pymongo.errors.OperationFailure as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
