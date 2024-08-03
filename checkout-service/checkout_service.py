from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/checkout', methods=['POST'])
def checkout():
    return jsonify({"message": "Checkout successful", "order_id": 123})

@app.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    return jsonify({"order_id": order_id, "status": "shipped", "items": ["item1", "item2"]})

if __name__ == '__main__':
    app.run(port=5002)
