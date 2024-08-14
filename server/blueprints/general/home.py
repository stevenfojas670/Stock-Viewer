from flask import Blueprint, request, redirect, url_for, g

# Defining a blueprint
home_bp = Blueprint(
    'home_bp', __name__,
)

@home_bp.route("/", methods=['GET'])
def home():
    if request.method == 'GET':
        return "Returning information"
    else:
        return "Home Page"