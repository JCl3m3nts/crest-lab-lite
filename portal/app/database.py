import sqlite3
from datetime import datetime


DATABASE = "/crest/data/crest.db"


def get_connection():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn



def get_questions():

    conn = get_connection()

    questions = conn.execute(
        """
        SELECT *
        FROM questions
        """
    ).fetchall()

    conn.close()

    return questions



def get_question(question_id):

    conn = get_connection()

    question = conn.execute(
        """
        SELECT *
        FROM questions
        WHERE id = ?
        """,
        (question_id,)
    ).fetchone()

    conn.close()

    return question



def get_trophy(question_id):

    conn = get_connection()

    trophy = conn.execute(
        """
        SELECT *
        FROM trophies
        WHERE question_id = ?
        """,
        (question_id,)
    ).fetchone()

    conn.close()

    return trophy



def check_answer(correct, supplied):

    return correct.lower().strip() == supplied.lower().strip()



def save_progress(question_id):

    conn = get_connection()

    existing = conn.execute(
        """
        SELECT *
        FROM progress
        WHERE question_id = ?
        """,
        (question_id,)
    ).fetchone()


    if existing is None:

        conn.execute(
            """
            INSERT INTO progress
            (
                question_id,
                completed,
                completed_at
            )
            VALUES (?,1,?)
            """,
            (
                question_id,
                datetime.now().isoformat()
            )
        )

        conn.commit()


    conn.close()



def get_progress():

    conn = get_connection()

    progress = conn.execute(
        """
        SELECT *
        FROM progress
        """
    ).fetchall()

    conn.close()

    return progress
def get_progress_summary():

    conn = get_connection()

    questions = conn.execute(
        """
        SELECT
            q.id,
            q.question,
            CASE
                WHEN p.completed = 1 THEN 1
                ELSE 0
            END AS completed
        FROM questions q
        LEFT JOIN progress p
            ON q.id = p.question_id
        ORDER BY q.id
        """
    ).fetchall()

    conn.close()

    return questions
