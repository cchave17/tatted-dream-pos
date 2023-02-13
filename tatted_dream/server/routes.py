from flask import Flask, render_template, jsonify

def create_routes(app):
    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/customers", methods=["GET"])
    def get_customers():
        # code to retrieve list of customers from database
        customers = [
            {"id": 1, "name": "John Doe"},
            {"id": 2, "name": "Jane Doe"},
            # ...
        ]

        return jsonify(customers)

    # Add additional routes here...
