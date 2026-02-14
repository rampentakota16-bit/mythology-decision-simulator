# ===============================
# Flask Web Application
# ===============================

from flask import Flask, jsonify, request, session


from mythology_simulator.data.questions import QUESTIONS
from mythology_simulator.core.scoring import calculate_average_positivity
from mythology_simulator.core.engine import map_average_to_character
from mythology_simulator.reports.analysis import generate_analytical_report

app = Flask(__name__)
app.secret_key = "mythology-secret-key"


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Mythology Decision Simulator API is running"
    })


@app.route("/start", methods=["GET"])
def start_quiz():
    return {
        "status": "ok",
        "message": "start reached"
    }


@app.route("/question", methods=["GET"])
def get_current_question():
    idx = session.get("current_index")

    if idx is None:
        return jsonify({"error": "Quiz not started"}), 400

    if idx >= len(QUESTIONS):
        return jsonify({"message": "Quiz completed"}), 200

    q = QUESTIONS[idx]

    return jsonify({
        "id": q["id"],
        "text": q["text"],
        "options": {
            k: v["label"] for k, v in q["options"].items()
        }
    })


@app.route("/answer", methods=["POST"])
def submit_answer():
    data = request.get_json()
    choice = data.get("choice")

    idx = session.get("current_index")
    responses = session.get("responses")

    if idx is None or responses is None:
        return jsonify({"error": "Quiz not started"}), 400

    if choice not in ["A", "B", "C", "D", "E"]:
        return jsonify({"error": "Invalid choice"}), 400

    positivity = QUESTIONS[idx]["options"][choice]["positivity"]
    responses.append(positivity)

    session["responses"] = responses
    session["current_index"] = idx + 1

    return jsonify({
        "message": "Answer recorded",
        "next_question_index": session["current_index"]
    })


@app.route("/questions", methods=["GET"])
def get_questions():
    """
    Returns all questions (for now).
    Later we will serve one question at a time.
    """
    return jsonify(QUESTIONS)


@app.route("/submit", methods=["POST"])
def submit_answers():
    """
    Expects JSON:
    {
        "responses": [100, 80, 50, ...]  # length = 30
    }
    """
    data = request.get_json()

    if not data or "responses" not in data:
        return jsonify({"error": "Responses not provided"}), 400

    responses = data["responses"]

    if len(responses) != len(QUESTIONS):
        return jsonify({"error": "Invalid number of responses"}), 400

    avg = calculate_average_positivity(responses)
    character = map_average_to_character(avg)

    return jsonify({
        "average_positivity": avg,
        "character": character
    })


@app.route("/report", methods=["POST"])
def generate_report():
    """
    Paid endpoint later.
    For now, returns report text.
    """
    data = request.get_json()

    character = data.get("character")
    average_positivity = data.get("average_positivity")

    if not character or average_positivity is None:
        return jsonify({"error": "Missing data"}), 400

    report = generate_analytical_report(character, average_positivity)

    return jsonify({
        "report": report
    })


if __name__ == "__main__":
    app.run()


