import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "crest.db"

conn = sqlite3.connect(DB)
c = conn.cursor()

# =========================================================
# TABLES
# =========================================================

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
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER NOT NULL UNIQUE,
    service TEXT NOT NULL,
    location TEXT,
    trophy_value TEXT NOT NULL,
    description TEXT,
    FOREIGN KEY(question_id) REFERENCES questions(id)
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER NOT NULL UNIQUE,
    completed INTEGER DEFAULT 0,
    completed_at TEXT
)
""")

# =========================================================
# ENUMERATION QUESTIONS
# =========================================================

questions = [
    (
        1, "SMB", "Beginner",
        "Download the trophy from the public SMB share.",
        "CREST-SMB-48291",
        "Find an SMB service.",
        "List the available shares.",
        "Use smbclient to download the file.",
        20
    ),
    (
        2, "FTP", "Easy",
        "Download the trophy from the anonymous FTP server.",
        "FTP_PUBLIC",
        "Identify the FTP service on TCP port 21.",
        "Try anonymous FTP access.",
        "List the available files and download trophy.txt.",
        20
    ),
    (
        3, "HTTP", "Easy",
        "Find and download the hidden web trophy.",
        "HTTP_SECRET",
        "Look for a web server.",
        "Check robots.txt.",
        "Enumerate directories to find the hidden location.",
        20
    ),
    (
        4, "SSH", "Easy",
        "Connect to the SSH server and retrieve the trophy.",
        "SSH_TROPHY",
        "Identify the SSH service using Nmap.",
        "Connect using the available SSH credentials.",
        "Search the filesystem for trophy.txt.",
        20
    ),
    (
        5, "DNS", "Medium",
        "Perform a DNS zone transfer and retrieve the hidden TXT record.",
        "DNS_TROPHY",
        "Identify the DNS service using Nmap.",
        "Attempt a zone transfer using dig AXFR.",
        "Look for hidden TXT records.",
        20
    ),
    (
        6, "SNMP", "Easy",
        "Enumerate the SNMP service and retrieve the SNMP extend trophy.",
        "NW-SNMP-001",
        "Check UDP port 161.",
        "Enumerate SNMP using the public community string.",
        "Look for NET-SNMP extend output.",
        10
    ),
    (
        7, "TELNET", "Easy",
        "Enumerate the Telnet service and retrieve the login trophy.",
        "TELNET_TROPHY",
        "Check TCP port 23.",
        "Connect using a Telnet client.",
        "Default credentials may be exposed.",
        10
    ),
    (
        8, "Finger", "Easy",
        "Enumerate the Finger service and retrieve the user information trophy.",
        "FINGER_TROPHY",
        "Check TCP port 79.",
        "Enumerate the Finger service for users.",
        "Inspect the information returned for the analyst account.",
        10
    ),
    (
        9, "LDAP", "Medium",
        "Enumerate the LDAP service and retrieve the user information trophy.",
        "LDAP_TROPHY",
        "Identify the LDAP service on TCP port 389.",
        "Enumerate the LDAP directory and inspect the People organisational unit.",
        "Look at the attributes of the jdoe account.",
        20
    ),
    (
        10, "SMTP", "Easy",
        "Enumerate the SMTP service and retrieve the SMTP user trophy.",
        "SMTP_TROPHY",
        "Check TCP port 25.",
        "Identify the SMTP hostname and banner.",
        "Investigate the exposed sales account and its home directory.",
        10
    ),
    (
        11, "POP3", "Easy",
        "Enumerate the POP3 service and retrieve the mailbox user's trophy.",
        "POP3_TROPHY",
        "Check TCP port 110.",
        "Identify the POP3 service and authentication methods.",
        "Investigate the exposed hr account and its home directory.",
        10
    ),
    (
        12, "IMAPS", "Medium",
        "Enumerate the secure IMAP service and retrieve the IMAPS user trophy.",
        "IMAPS_TROPHY",
        "Check TCP port 993.",
        "Inspect the IMAPS TLS certificate and service.",
        "Investigate the exposed imapuser account and its home directory.",
        20
    ),
    (
        13, "RSH", "Medium",
        "Enumerate the RSH service and retrieve the remote-shell user trophy.",
        "RSH_TROPHY",
        "Check TCP port 514.",
        "Identify the RSH service and investigate trust relationships.",
        "Investigate the operator account and RSH configuration.",
        20
    ),
    (
        14, "RDP", "Medium",
        "Enumerate the RDP service and retrieve the RDP user trophy.",
        "RDP_TROPHY",
        "Check TCP port 3389.",
        "Identify the xrdp service and target hostname.",
        "Connect using the exposed rdpuser account and inspect its home directory.",
        20
    )
]

# =========================================================
# ENUMERATION TROPHIES
# =========================================================

trophies = [
    (
        1, "SMB",
        r"\\NW-FILE01\public\trophy.txt",
        "CREST-SMB-48291",
        "Public SMB share trophy"
    ),
    (
        2, "FTP",
        "/pub/trophy.txt",
        "CREST-FTP-73942",
        "Anonymous FTP trophy"
    ),
    (
        3, "HTTP",
        "/secret/trophy.txt",
        "CREST-HTTP-92841",
        "Hidden web trophy"
    ),
    (
        4, "SSH",
        "/opt/trophies/trophy.txt",
        "CREST-SSH-56291",
        "SSH filesystem trophy"
    ),
    (
        5, "DNS",
        "northwind.local TXT record",
        "CREST-DNS-78124",
        "DNS TXT record trophy"
    ),
    (
        6, "SNMP",
        "SNMP extend output",
        "NW-SNMP-001",
        "SNMP extend trophy"
    ),
    (
        7, "TELNET",
        "Telnet login",
        "NW-TELNET-001",
        "Telnet login trophy"
    ),
    (
        8, "Finger",
        "Finger user information",
        "NW-FINGER-001",
        "Finger user information trophy"
    ),
    (
        9, "LDAP",
        "uid=jdoe,ou=People,dc=northwind,dc=local",
        "CREST-LDAP-59381",
        "LDAP user information trophy"
    ),
    (
        10, "SMTP",
        "/home/sales/smtp_trophy.txt",
        "CREST-SMTP-84216",
        "SMTP user filesystem trophy"
    ),
    (
        11, "POP3",
        "/home/hr/pop3_trophy.txt",
        "CREST-POP3-39527",
        "POP3 mailbox user trophy"
    ),
    (
        12, "IMAPS",
        "/home/imapuser/imaps_trophy.txt",
        "CREST-IMAPS-61527",
        "IMAPS user filesystem trophy"
    ),
    (
        13, "RSH",
        "/home/operator/rsh_trophy.txt",
        "CREST-RSH-66318",
        "RSH remote-shell user trophy"
    ),
    (
        14, "RDP",
        "/home/rdpuser/rdp_trophy.txt",
        "CREST-RDP-51842",
        "RDP user filesystem trophy"
    )
]

# =========================================================
# RESET ENUMERATION DATA
# =========================================================

c.execute("DELETE FROM progress")
c.execute("DELETE FROM trophies")
c.execute("DELETE FROM questions")

# =========================================================
# INSERT QUESTIONS
# =========================================================

c.executemany("""
INSERT INTO questions
(
    id,
    category,
    difficulty,
    question,
    answer_key,
    hint1,
    hint2,
    hint3,
    points
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", questions)

# =========================================================
# INSERT TROPHIES
# =========================================================

c.executemany("""
INSERT INTO trophies
(
    question_id,
    service,
    location,
    trophy_value,
    description
)
VALUES (?, ?, ?, ?, ?)
""", trophies)

conn.commit()

# =========================================================
# VALIDATION
# =========================================================

question_count = c.execute(
    "SELECT COUNT(*) FROM questions"
).fetchone()[0]

trophy_count = c.execute(
    "SELECT COUNT(*) FROM trophies"
).fetchone()[0]

total_points = c.execute(
    "SELECT COALESCE(SUM(points), 0) FROM questions"
).fetchone()[0]

print()
print("==============================================")
print(" CREST LAB DATABASE INITIALISED")
print("==============================================")
print(f" Enumeration questions : {question_count}")
print(f" Enumeration trophies  : {trophy_count}")
print(f" Total points          : {total_points}")
print("==============================================")

if question_count != 14:
    raise SystemExit("ERROR: Expected 14 questions")

if trophy_count != 14:
    raise SystemExit("ERROR: Expected 14 trophies")

print("Database validation: PASS")

conn.close()
