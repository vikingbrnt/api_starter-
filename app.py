from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong"})


@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route("/users", methods=["GET"]) 
def get_users(): 
    conn = mysql.connector.connect( host="mysql-serhal.alwaysdata.net", user="serhal", password="454-AJK-0101/", database="serhal_projct" ) 
    
    cursor = conn.cursor(dictionary=True) 
    
    cursor.execute("SELECT * FROM users_id;") 
    
    rows = cursor.fetchall() 
    
    cursor.close() 
    
    conn.close() 
    
    return jsonify(rows)
@app.route("/users", methods=["POST"])
def create_user():

    data = request.get_json()
    name = data.get("name")

    if not name:
        return jsonify({"error": "name is required"}), 400

    conn = mysql.connector.connect(
        host="mysql-serhal.alwaysdata.net",
        user="serhal",
        password="545-AJK-0101/",
        database="serhal_projct"
    )

    cursor = conn.cursor()

    cursor.execute("INSERT INTO users_id (name) VALUES (%s)", (name,))
    conn.commit()

    new_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return jsonify({"id": new_id, "name": name}), 201


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):

    data = request.get_json()
    name = data.get("name")

    if not name:
        return jsonify({"error": "name is required"}), 400

    conn = mysql.connector.connect(
        host="mysql-serhal.alwaysdata.net",
        user="serhal",
        password="454-AJK-0101/",
        database="serhal_projct"
    )

    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users_id SET name=%s WHERE id=%s",
        (name, user_id)
    )

    conn.commit()

    updated = cursor.rowcount

    cursor.close()
    conn.close()

    if updated == 0:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"id": user_id, "name": name})

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):

    conn = mysql.connector.connect(
        host="mysql-serhal.alwaysdata.net",
        user="serhal",
        password="454-AJK-0101/",
        database="serhal_projct"
    )

    cursor = conn.cursor()

    cursor.execute("DELETE FROM users_id WHERE id=%s", (user_id,))
    conn.commit()

    deleted = cursor.rowcount

    cursor.close()
    conn.close()

    if deleted == 0:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": "User deleted"})

if __name__ == "__main__":
    app.run(port=4996, debug=True)