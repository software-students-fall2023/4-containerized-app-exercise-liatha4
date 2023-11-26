import os
from flask import Flask, request, jsonify
import base64
import cv2
import numpy as np
from face import process_emotion  
import pymongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# client = pymongo.MongoClient("mongodb://db:27017")
# db = client["faces"]  
# collection = db["expressions"]     

@app.route("/image", methods=["POST"])
def upload_image():
    """Route for parsing image received from webcam into expression data"""
    data = request.json
    if not data or "image" not in data:
        return "No image data", 400

    image_data = data["image"]
    encoded_data = image_data.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    emotion_result = process_emotion(img)

    try:
        # document = {"output": emotion_result}
        # collection.insert_one(document)
        return jsonify(emotion_result), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
