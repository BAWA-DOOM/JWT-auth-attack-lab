from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)
SECRET = "supersecretkey"

@app.route("/login", methods=["POST"])
def login():
    user = request.json.get("user")

    token = jwt.encode(
        {"user": user, "role": "user"},
        SECRET,
        algorithm="HS256"
    )

    return jsonify({"token": token})

@app.route("/admin")
def admin():
    token = request.headers.get("Authorization")

    try:
        decoded = jwt.decode(
            token,
            SECRET,
            algorithms=["HS256"]  # ✅ FIX
        )
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid Token"}), 401

    if decoded.get("role") == "admin":
        return jsonify({"message": "Welcome Admin!"})

    return jsonify({"error": "Access Denied"}), 403

if __name__ == "__main__":
    app.run(debug=True)
