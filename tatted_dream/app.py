import base64

from flask import Flask, render_template, request, redirect, url_for

from tatted_dream.data_utils import get_all_customers, execute_sql, add_new_customer

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.template_filter()
def b64encode(s):
    return base64.b64encode(s).decode('utf-8')

@app.route('/customers')
def customers():
    return render_template('customers.html')


@app.route("/view_customers")
def view_customers():
    # Get the list of customers from the database
    customers = get_all_customers()

    for customer in customers:
        if customer['Photo_ID'] is not None:
            customer['Photo_ID'] = base64.b64encode(customer['Photo_ID']).decode('utf-8')
        else:
            customer['Photo_ID'] = None

        if customer['Signature'] is not None:
            customer['Signature'] = base64.b64encode(customer['Signature']).decode('utf-8')
        else:
            customer['Signature'] = None

    # Render the view_customers.html template and pass the list of customers to it
    return render_template("view_customers.html", customers=customers)






@app.route("/add_customer", methods=["GET", "POST"])
def add_customer():
    if request.method == "POST":
        # Get the customer information from the form
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        gender = request.form.get("gender")
        photo_id = request.files.get("photo_id")
        signature = request.files.get("signature")

        # Read the image data

        photo_id_data = photo_id.read() if photo_id else None
        signature_data = signature.read() if signature else None

        # Insert the customer information into the database
        add_new_customer(name, email, phone, gender, photo_id_data, signature_data)
        # Redirect the user back to the customers page
        return redirect(url_for("customers"))

    # If it's a GET request, render the form for adding a new customer
    return render_template("add_customer.html")
