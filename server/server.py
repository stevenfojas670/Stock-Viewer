import os
from flask import Flask, redirect, url_for, request, jsonify, url_for, g
from flask_caching import Cache
from markupsafe import escape
from flask_cors import CORS

# Blueprints imports
from blueprints.general.home import home_bp
from blueprints.auth.signup import registration_bp
from blueprints.auth.login import login_bp

app = Flask(__name__)
CORS(app)

app.config['AV_KEY'] = os.environ.get('AV_KEY')
app.config['SECRET_KEY'] = os.environ.get('JWT_KEY')


# Going to need a teardown request to clear the global variable

# Registering blueprints
app.register_blueprint(home_bp)
app.register_blueprint(registration_bp)
app.register_blueprint(login_bp)


if __name__ == "__main__":
    app.run(port=8080, debug=True)