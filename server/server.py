import os
from flask import Flask, redirect, url_for, request, jsonify, url_for, g
from flask_caching import Cache
from markupsafe import escape
from flask_cors import CORS
from pymongo import MongoClient

# Blueprints imports
from blueprints.general.home import home_bp
from blueprints.auth.signup import registration_bp
from blueprints.auth.login import login_bp

app = Flask(__name__)
CORS(app)

app.config['AV_KEY'] = os.environ.get('AV_KEY')
app.config['SECRET_KEY'] = os.environ.get('JWT_KEY')

client = MongoClient('localhost', 27017)
db = client['StockTrackerDB']
users_collection = db['Users']

@app.before_request
def before_request():
    g.db = db

# Going to need a teardown request to clear the global variable

# Registering blueprints
app.register_blueprint(home_bp)
app.register_blueprint(registration_bp)
app.register_blueprint(login_bp)


if __name__ == "__main__":
    app.run(port=8080, debug=True)