from flask import Flask, redirect, request, render_template    # Import flask framwork into python code
app = Flask(__name__)       # creates the flask application object

@app.route("/")             # Define the URL route "/".
def hello():                # This is python function
    return "Hello World"    # this text as the webpafe response

@app.route("/home")         # Define the URL route "/home"
def home():
    return "This is Home page"

@app.route("/user", methods=["GET", "POST"])  # Define the URL route "/user" and specify the allowed HTTP methods (GET and POST)

def user():

    if request.method == "POST":

        try:
            # Get data from frontend form
            name = request.form["name"]
            age = request.form["age"]
            email = request.form["email"]

            # Insert data into MongoDB
            User_control.insert_user(name, age, email)

            # Redirect after successful insertion
            return redirect("/success")
        except Exception as e:

            # Stay on same page and display error
            return render_template(
                "user_form.html",
                error=str(e)
            )
    return render_template("user_form.html")

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)

import User_control   # Import the User_control.py file into app.py
import data_json.api as api  # Import the data_json/api.py file into app.py