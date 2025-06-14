import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Hello from Flask!"


@app.route("/api/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify({"you_said": data.get("message", "")})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
