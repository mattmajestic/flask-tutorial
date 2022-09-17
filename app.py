from flask import Flask, render_template, jsonify
from datetime import datetime
import re
from flask_swagger import swagger

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "home.html"
    )

# This returns our HTML template passing in the URL string dynamically
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "index.html",
        name=name,
        date=datetime.now()
    )
    
# This serves the data in our static/data.json
@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

# This is the Swagger API
@app.route("/spec")
def spec():
    return jsonify(swagger(app))