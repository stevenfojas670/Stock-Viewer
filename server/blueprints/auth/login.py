from flask import Blueprint

# Defining a blueprint
login_bp = Blueprint(
    'login_bp', __name__,
)

@login_bp.route("/login", methods=['GET', 'POST'])
def registration():
    return "Login page!"