from flask import Flask, render_template, request

from database import (
    get_questions,
    get_question,
    get_trophy,
    save_progress,
    get_progress,
    get_progress_summary,
    validate_trophy
)


app = Flask(__name__)


@app.route("/")
def index():

    questions = get_questions()

    return render_template(
        "index.html",
        questions=questions
    )

@app.route("/question/<int:id>", methods=["GET", "POST"])
def question(id):

    current = get_question(id)
    trophy = get_trophy(id)

    if current is None:
        return "Question not found", 404


    result = None
    hint = None


    if request.method == "POST":

        action = request.form.get("action")


        if action == "answer":

            answer = request.form["answer"]

            if validate_trophy(
                id,
                answer
            ):
                result = "correct"
                save_progress(id)

            else:
                result = "incorrect"


        elif action == "hint":

            hint_number = int(
                request.form.get("hint_number", 1)
            )


            if hint_number == 1:
                hint = current["hint1"]

            elif hint_number == 2:
                hint = current["hint2"]

            elif hint_number == 3:
                hint = current["hint3"]



    return render_template(
        "question.html",
        question=current,
        result=result,
        hint=hint
    )


@app.route("/progress")
def progress():

    questions = get_progress_summary()

    completed = sum(
        1 for q in questions
        if q["completed"]
    )

    return render_template(
        "progress.html",
        questions=questions,
        completed=completed,
        total=len(questions)
    )
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=80
    )
