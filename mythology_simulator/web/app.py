from flask import Flask, jsonify

app = Flask(__name__)
app.secret_key = "mythology-secret-key"

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "_toggle_ok_"})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})

@app.route("/start", methods=["GET"])
def start():
    return jsonify({
        "message": "Quiz started",
        "total_questions": 30
    })
