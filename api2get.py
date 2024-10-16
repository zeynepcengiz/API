from flask import Flask,jsonify

app= Flask(__name__)

@app.route("/api/resource/", methods = ["GET"])

def get_resource():
    return jsonify({"message": "Resource retrieved successfully."})

if __name__ == "__main__":
    app.run(debug=True)