from flask import Blueprint, request, redirect, url_for, g

# Defining a blueprint
registration_bp = Blueprint(
    'registration_bp', __name__,
)

@registration_bp.route("/register", methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        db = g.db
        users_collection = db['Users']

        username = request.form['username']
        password = request.form['password']

        # Check if username already exists
        if users_collection.find_one({'username': username}):
            print("In use")
        else:
            users_collection.insert_one({'username': username, 'password': password})
            return redirect(url_for('login'))
    else:
        return "Nothing"