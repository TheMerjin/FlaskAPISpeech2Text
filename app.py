from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows Astro frontend to talk to Flask


@app.route("/")
def home():
    return "Hello from Flask!"


@app.route("/api/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify({"you_said": data.get("message", "")})


if __name__ == "__main__":
    app.run()
