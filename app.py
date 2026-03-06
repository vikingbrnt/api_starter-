from flask import Flask, jsonify
from database import get_connection

app = Flask(__name__)


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong"})


@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, World!"})


@app.route("/users", methods=["GET"])
def get_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(rows)


if __name__ == "__main__":
    app.run(port=4996, debug=True)