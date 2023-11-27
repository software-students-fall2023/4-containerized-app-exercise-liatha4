from flask import Flask, render_template
from flask_cors import CORS
from pymongo import MongoClient
from flask_cors import CORS
from dotenv import load_dotenv
import os

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
    return render_template("index.html")

@app.route('/happy_route')
def happy():
    return render_template("happy.html")

@app.route('/sad_route')
def sad():
    return render_template("sad.html")

@app.route('/angry_route')
def angry():
    return render_template("angry.html")

@app.route('/surprised_route')
def surprised():
    return render_template("surprised.html")

@app.route('/fear_route')
def fear():
    return render_template("fear.html")

@app.route('/expressions')
def expressions():
    data = facedata.find()
    return render_template("expressions.html",data=data)
    

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3001)  
