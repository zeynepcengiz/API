import requests
from flask import Flask, jsonify

app = Flask(__name__)

gorev =[]

@app.route("/api/gorev", methods=["GET"])

def get_gorev():
    return jsonify(gorev)

@app.route("/api/gorev", methods=["POST"])

def post_gorev():
    gorev2= requests.get_json()
    if "gorev" not in gorev2 or "name" not in gorev2:
        return jsonify({"error" : "Name and gorev not found."})
    gorev2["id"] = len(gorev)+1
    gorev.append(gorev2)
    return jsonify(gorev2) ,201

@app.route("/api/gorev/<int:gorev2_id>" , methods =["PUT"])

def update_gorev():
    gorev2 = next((gorev2 for gorev2 in gorev if gorev["id"] == gorev2_id),None)
    if gorev2:
        data = requests.get_json()
        gorev2.update(data)
        return jsonify()
    return jsonify({"error": "Gorev not found."}),404

if __name__ == "__main__":
    app.run(debug=True)