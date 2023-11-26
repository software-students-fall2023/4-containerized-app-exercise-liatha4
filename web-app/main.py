from flask import Flask, render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

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

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3001)  
