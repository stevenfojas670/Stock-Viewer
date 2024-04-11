from flask import Flask, redirect, url_for, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)