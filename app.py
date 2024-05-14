from flask import Flask, render_template, request , redirect, url_for
from db import Database

app = Flask(__name__)
dbo = Database()


@app.route('/')
def index():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("Register.html")


@app.route('/perform_register', methods=['post'])
def perform_register():
    name = request.form.get("user_name")
    email = request.form.get("user_email")
    password = request.form.get("user_password")
    response = dbo.insert(name, email, password)

    if response == 1:
        return render_template("login.html", message="Registration Successful. Kindly Login to proceed")
    else:
        return render_template("Register.html", message="Email already registered")


@app.route('/perform_login', methods=['post'])
def perform_login():
    email = request.form.get("user_email")
    password = request.form.get("user_password")
    response = dbo.search(email, password)

    if response == 1:

        return redirect("/profile")
    else:

        return render_template("Register.html","Invalid Credentials")



@app.route('/profile')
def profile():
    return render_template("profile.html")


@app.route('/ner')
def ner():
    return render_template("ner.html")

@app.route('/perform_ner',methods=['post'])
def perform_ner():
    test=request.form.get("ner_test")

app.run(debug=True)
