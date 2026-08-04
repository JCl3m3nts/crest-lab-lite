import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "crest.db"

conn = sqlite3.connect(DB)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY,
    category TEXT NOT NULL,
    difficulty TEXT NOT NULL,
    question TEXT NOT NULL,
    answer_key TEXT NOT NULL,
    hint1 TEXT,
    hint2 TEXT,
    hint3 TEXT,
    points INTEGER DEFAULT 10
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS trophies (
    answer_key TEXT PRIMARY KEY,
    value TEXT NOT NULL
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER NOT NULL,
    completed INTEGER DEFAULT 0,
    completed_at TEXT
)
""")

questions = [
    (
        1,
        "SMB",
        "Beginner",
        "Download the trophy from the public SMB share.",
        "SMB_PUBLIC",
        "Find an SMB service.",
        "List the available shares.",
        "Use smbclient to download the file.",
        20
    )
]

trophies = [
    (
        "SMB_PUBLIC",
        "CREST-SMB-48291"
    )
]

c.executemany("""
INSERT OR REPLACE INTO questions
VALUES (?,?,?,?,?,?,?,?,?)
""", questions)

c.executemany("""
INSERT OR REPLACE INTO trophies
VALUES (?,?)
""", trophies)

conn.commit()
conn.close()

print("Database created successfully.")
