# Flask API with MongoDB

# Objective

Build a Flask application that includes a JSON API route at /api, which reads data from a backend file and returns it as a JSON response, and a frontend form that submits user data to MongoDB Atlas with proper success and error handling; on successful submission, the user is redirected to a page showing “Data submitted successfully,” while any failure keeps the user on the same page and displays the error message without redirecting.

# Download & Setup

## Step-1: Creating & activating venv Windows:

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

### Task 1: JSON API Route

Create a Flask application with an /api route. When this route is accessed, it should return a JSON list. The data should be stored in a backend file, read from it, and sent as a response.


This assignment is a simple Flask web application that demonstrates basic routing, Python module imports, and creating a JSON API using data stored in a JSON file.

## Features

- Flask application setup
- Home (`/`) route
- `/home` route
- `/api` route for JSON data
- Reads user data from `data.json`
- Returns JSON response using Flask `jsonify()`

## Project Structure

```text
project/
│
├── app.py
├── User_control.py
│
└── data_json/
    ├── api.py
    └── data.json
