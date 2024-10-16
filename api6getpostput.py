import requests
from flask import Flask, jsonify

app = Flask(__name__)

product=[]

@app.route("/api/product", methods=["GET"])

def get_product():
    return jsonify(product)

@app.route("/api/product" ,methods = ["POST"])

def post_product():
    product2 = requests.get_json()
    if "name" not in product2:
        return jsonify({"error": "Name not found."}),400
    product2["name"] = len(product)+1
    product2["completed"] = False
    product.append(product2),201

@app.route("/api/product/<int:product_name>" , methods = ["PUT"])

def update_product():
    product2 = next((product2 for product2 in product if product2["name"]== product_name),None)
    if product2 :
        data= requests.get_json()
        product2.update(data)
        return jsonify(product2)
    return jsonify({"error": "Product2 not found."})

if __name__ == "__main__":
    app.run(debug=True)