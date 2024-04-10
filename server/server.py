from flask import Flask, redirect, url_for, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/<name>") #/<name> is a dynamic route that accepts a string as a parameter
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!")) # redirects to the home route

@app.route("/login", methods=["POST", "GET"]) # methods is used to define if we are posting or getting data
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", name=user))
    else:
        return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)