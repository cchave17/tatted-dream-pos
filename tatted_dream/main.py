"""

"""
from flask import Flask, render_template, jsonify

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/customers", methods=["GET"])
def get_customers():
    # code to retrieve list of customers from database
    customers = [
        {"id": 1, "name": "John Doe"},
        {"id": 2, "name": "Jane Doe"}
        # ...
    ]

    return jsonify(customers)

