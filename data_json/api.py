from app import app
import json             
from flask import jsonify

@app.route("/api")
def api():
    with open("data_json/data.json", "r", encoding="utf-8") as file:  # opens data.json JSON file
        data = json.load(file)      #  reads the JSON content into Python

    return jsonify(data)        # returns it as JSON response to the browser


# if you want to run this file directly, you can uncomment the following lines

# if __name__ == "__main__":      # the file you started directly
#     app.run(debug=True)         # start the web server