import requests
from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/api/resource", methods = ["POST"])

def post_resource():
    data = requests.get_json()
    return jsonify({"data": data,"message" : "POST request successfully."})

if __name__ == "__main__":
    app.run(debug=True)