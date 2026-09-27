from app import app

@app.route("/about")
def about():
    return "This is flask application"