"""
A flask-app frontend that communicates with a mongodb instance and a 
seperate flask backend. This application allows users to take
pictures of themselves and send them to the DeepFace module
running in a separate flask app, and then depending
on the processed facial expression be redirected to a relevant 
emotional landing page
"""

import os
from flask import Flask, render_template, redirect
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
CORS(app)


def get_mongo_client(uri):
    """Create and return a MongoDB client."""
    return MongoClient(uri)


mongo_uri = os.getenv("MONGO_URI")
client = get_mongo_client(mongo_uri)
db = client[os.getenv("MONGO_DBNAME")]
fancy = db.fancies
facedata = db.facedata


@app.route("/")
def index():
    """
    Default page
    """
    return render_template("index.html")


@app.route("/happy_route")
def happy():
    """
    Page for happy users
    """
    return render_template("happy.html")


@app.route("/sad_route")
def sad():
    """
    Page for sad users
    """
    return render_template("sad.html")


@app.route("/angry_route")
def angry():
    """
    Page for angry users
    """
    return render_template("angry.html")


@app.route("/surprised_route")
def surprised():
    """
    Page for surprised users
    """
    return render_template("surprised.html")


@app.route("/fear_route")
def fear():
    """
    Page for scared users
    """
    return render_template("fear.html")


@app.route("/expressions")
def expressions():
    """
    Page for accessing the emotional data from facial scans.
    Pulls from mongodb
    """
    data = facedata.find()
    return render_template("expressions.html", data=data)


@app.route("/fancytown")
def fancytown():
    """
    A Page for users to look at themselves and press a button that tells
    them they are looking fancy.
    Pulls from mongodb
    """
    fancies = fancy.find({})
    return render_template("fancytown.html", fancies=fancies)


@app.route("/upload", methods=["POST"])
def upload_image():
    """
    A route for uploading a fancy message
    """
    document = {"feeling": "fancy"}
    fancy.insert_one(document)
    fancies = fancy.find({})
    print(fancies)
    return redirect("fancytown")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3001)
