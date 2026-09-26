from flask import Flask     # Import flask framwork into python code
app = Flask(__name__)       # creates the flask application object

@app.route("/")             # Define the URL route "/".
def hello():                # This is python function
    return "Hello World"    # this text as the webpafe response

@app.route("/home")         # Define the URL route "/home"
def home():
    return "This is Home page"

import User_control   # Import the User_control.py file into app.py