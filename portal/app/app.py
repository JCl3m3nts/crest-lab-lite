from flask import Flask, render_template, request, redirect
import json
import os


app = Flask(__name__)


QUESTION_FILE = "/crest/data/questions.json"


def load_questions():
    with open(QUESTION_FILE, "r") as file:
        return json.load(file)


@app.route("/")
def index():

    questions = load_questions()

    return render_template(
        "index.html",
        questions=questions
    )


@app.route("/question/<int:id>", methods=["GET", "POST"])
def question(id):

    questions = load_questions()

    current = next(
        (q for q in questions if q["id"] == id),
        None
    )

    if current is None:
        return "Question not found", 404


    result = None


    if request.method == "POST":

        answer = request.form["answer"].lower().strip()

        if answer == current["answer"].lower():
            result = "correct"
        else:
            result = "incorrect"


    return render_template(
        "question.html",
        question=current,
        result=result
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=80
    )
