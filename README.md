# Flask API with MongoDB

# Objective

Build a Flask application that includes a JSON API route at /api, which reads data from a backend file and returns it as a JSON response, and a frontend form that submits user data to MongoDB Atlas with proper success and error handling; on successful submission, the user is redirected to a page showing “Data submitted successfully,” while any failure keeps the user on the same page and displays the error message without redirecting.

# Download & Setup

## Step-1: Creating & activating venv linux:

```bash
python -m venv venv
source venv/bin/activate
```

## Step-2: Running application 

```bash
export PYTHONDONTWRITEBYTECODE=1 FLASK_APP="app" FLASK_ENV="development"
flask run
```

## Common issue

debuging off to on

```bash
export FLASK_DEBUG=1
```

Prevent pycham file

```bash
export PYTHONDONTWRITEBYTECODE=1
```

# Flask User Registration with MongoDB Atlas $ backend 

This project is a Flask web application that collects user information through a frontend form and stores the data in MongoDB Atlas.

## Features

- Modern and responsive user registration form
- Flask backend
- MongoDB Atlas database integration
- Stores Name, Age, and Email
- Success page after successful submission
- Displays errors on the same page
- Environment variables used for database credentials

## Project Structure

```text
Flask-MongoDB/
│
├── app.py
├── user_control.py
├── test_mongodb.py
├── .env
├── .gitignore
│
└── templates/
    ├── user_form.html
    └── success.html
