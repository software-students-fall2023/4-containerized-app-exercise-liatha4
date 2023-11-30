from flask import Flask, request, jsonify,render_template,redirect
import base64
from flask_cors import CORS
from pymongo import MongoClient
import gridfs
from dotenv import load_dotenv
import os
import codecs

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



@app.route('/fancytown')
def fancytown():
    fancies = fancy.find({})
    return render_template("fancytown.html",fancies=fancies)

@app.route('/upload', methods=['POST'])
def upload_image():
    document = {"feeling":"fancy"}
    fancy.insert_one(document)
    fancies = fancy.find({})
    print(fancies)
    return redirect("fancytown")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3001)  
