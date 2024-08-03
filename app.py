from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    return jsonify({"message": "User logged in", "user_id": 1})

@app.route('/signup', methods=['POST'])
def signup():
    return jsonify({"message": "User signed up", "user_id": 2})

@app.route('/logout', methods=['POST'])
def logout():
    return jsonify({"message": "User logged out"})


@app.route('/checkout', methods=['POST'])
def checkout():
    return jsonify({"message": "Checkout successful", "order_id": 123})

@app.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    return jsonify({"order_id": order_id, "status": "shipped", "items": ["item1", "item2"]})

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
    app.run(port=5001)