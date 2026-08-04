from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():

    questions = [
        "How many open ports exist?",
        "What is the hostname?",
        "Find the FTP trophy",
        "Find the SMB trophy",
        "Find the LDAP trophy"
    ]

    return render_template(
        "index.html",
        questions=questions
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=80
    )
