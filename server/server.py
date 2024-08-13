import os 
import requests
from flask import Flask, redirect, url_for, request, jsonify, url_for
from flask_caching import Cache
from markupsafe import escape
from flask_cors import CORS
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

API_KEY = os.getenv("AV_KEY")

app = Flask(__name__)
CORS(app)

client = MongoClient('localhost', 27017, username='admin', password='admin')

db = client.flask_db
todos = db.todos


@app.route("/", strict_slashes=False, methods=['GET'])
def home():
    if request.method == 'GET':
        return "Home Page"


if __name__ == "__main__":
    app.run(port=8080, debug=True)