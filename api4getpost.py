from flask import Flask, jsonify, request

app = Flask(__name__)

users = []

@app.route("/api/zeze", methods = ["GET"])

def get_zeze():
    return jsonify(users)

@app.route("/api/zeze", methods = ["POST"])

def post_zeze():
    user = request.get_json()
    if "name" not in user or "email" not in user:
        return jsonify({"error" : "Name or email are required."}),400
    user["id"] = len(users)+1
    users.append(user)
    return jsonify(user),201

@app.route("/api/zeze/<int:user_id>" ,methods = ["PUT"])

def update_zeze():
    user = next((user for user in users if user ["id"] == user_id),None)
    if user:
        data = request.get_json()
        user.update(data)
        return jsonify({"error": "User not found."}),404
    
if __name__ == "__main__":
    app.run(debug=True)