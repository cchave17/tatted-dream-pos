from flask import Flask, render_template, url_for, request
import os
from tatted_dream.server.email.message import Message, construct_email
from tatted_dream.server.email.send_email import send_email

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/index", methods=["POST"])
def book_appointment():
    data = {}
    if request.method == "POST":
        data = request.form.to_dict()

        msg = Message(data).get_msg()
        email_content = construct_email(msg)

        send_email(email_content)

    return render_template("index.html")
