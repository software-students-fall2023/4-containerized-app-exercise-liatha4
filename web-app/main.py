"""
This module provides routes for a Flask web application interfacing with MongoDB,
handling different emotional routes and rendering respective HTML templates.
"""

import os
from flask import Flask, render_template
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
facedata = db.facedata

@app.route('/')
def index():
    """Render the index page."""
    return render_template("index.html")

@app.route('/happy_route')
def happy():
    """Render the happy emotion page."""
    return render_template("happy.html")

@app.route('/sad_route')
def sad():
    """Render the sad emotion page."""
    return render_template("sad.html")

@app.route('/angry_route')
def angry():
    """Render the angry emotion page."""
    return render_template("angry.html")

@app.route('/surprised_route')
def surprised():
    """Render the surprised emotion page."""
    return render_template("surprised.html")

@app.route('/fear_route')
def fear():
    """Render the fear emotion page."""
    return render_template("fear.html")

@app.route('/expressions')
def expressions():
    """Fetch and display expressions data."""
    data = facedata.find()
    return render_template("expressions.html", data=data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3001)
