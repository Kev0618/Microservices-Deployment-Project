from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify([
        {"product_id": 1, "name": "Product 1", "price": 100},
        {"product_id": 2, "name": "Product 2", "price": 150}
    ])

@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    return jsonify({"product_id": product_id, "name": f"Product {product_id}", "price": 100 + product_id * 50})

if __name__ == '__main__':
    app.run(port=5003)
