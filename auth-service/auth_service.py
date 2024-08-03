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

if __name__ == '__main__':
    app.run(port=5001)
