"""
This file contains all of the endpoints for our flask app.
"""
from http import HTTPStatus

from flask import Flask, request  # type: ignore -> , request
from flask_restx import Resource, Api, fields   # type: ignore -> Namespace
from flask_cors import CORS  # type: ignore
import werkzeug.exceptions as wz  # type: ignore

# Start Flask App
app = Flask(__name__)
CORS(app)
api = Api(app)

@app.route("/")
def hello():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
