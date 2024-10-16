import requests
from flask import Flask, jsonify

app = Flask(__name__)

blog =[]

@app.route("/api/blog" , methods = ["GET"])

def get_blog():
    return jsonify

@app.route("/api/blog", methods =["POST"])

def post_blog():
    blog2 = requests.get_json()
    if "id" not in blog2:
        return jsonify({"error" : "ID not found."}),400
    blog2["id"] = len(blog)+1
    blog["completed"] = False
    blog.append(blog2), 201

@app.route('/api/blog/<int:blog_id>', methods = ["PUT"])

def update_blog():
    blog2= next((blog2 for blog2 in blog if blog2["id"] == blog_id),None)
    if blog2:
        data = requests.get_json()
        blog2.update(data)
        return jsonify(blog2)
    return jsonify({"error": "Blog2 not found."})

if __name__ == "__main__":
    app.run(debug=True)