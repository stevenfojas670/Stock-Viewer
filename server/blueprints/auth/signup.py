from flask import Blueprint, request

# Defining a blueprint
registration_bp = Blueprint(
    'registration_bp', __name__,
)

@registration_bp.route("/register", methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username already exists