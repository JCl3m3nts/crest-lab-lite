# CREST-Lab Lite

A Docker-based cybersecurity enumeration training environment for practising reconnaissance, service enumeration and evidence gathering in a controlled local laboratory.

CREST-Lab Lite simulates the **Northwind Manufacturing Ltd** environment using Docker containers. It contains 14 network services, 14 enumeration questions, 14 trophies and a Flask-based training portal.

> **Educational use only.** The services are intentionally configured for security training. Only deploy and test this laboratory on systems and networks you own or have explicit permission to assess.

## Features

- 14 network services
- 14 enumeration challenges
- 14 trophies
- 230 total points
- Flask training portal
- SQLite question database
- Trophy validation
- Progress tracking
- Question difficulty ratings
- Static Docker network
- Designed for Kali Linux
- Repeatable Docker Compose deployment

## Services

| Q | Service | Hostname | IP | Port | Difficulty | Points |
|---|---|---|---|---|---|---:|
| 1 | SMB | NW-FILE01 | 172.30.0.20 | 139/445 | Beginner | 20 |
| 2 | FTP | FTP-SERVER01 | 172.30.0.30 | 21 | Easy | 20 |
| 3 | HTTP | WEB-SERVER01 | 172.30.0.40 | 80 | Easy | 20 |
| 4 | SSH | LINUX-JUMP01 | 172.30.0.50 | 22 | Easy | 20 |
| 5 | DNS | DNS-SERVER01 | 172.30.0.60 | 53 TCP/UDP | Medium | 20 |
| 6 | SNMP | SNMP01 | 172.30.0.90 | 161 UDP | Easy | 10 |
| 7 | Telnet | TELNET-SERVER01 | 172.30.0.100 | 23 | Easy | 10 |
| 8 | Finger | FINGER-SERVER01 | 172.30.0.110 | 79 | Easy | 10 |
| 9 | LDAP | LDAP-SERVER01 | 172.30.0.70 | 389 | Medium | 20 |
| 10 | SMTP | smtp.northwind.local | 172.30.0.140 | 25 | Easy | 10 |
| 11 | POP3 | pop3.northwind.local | 172.30.0.150 | 110 | Easy | 10 |
| 12 | IMAPS | imap.northwind.local | 172.30.0.160 | 993 | Medium | 20 |
| 13 | RSH | RSH-SERVER01 | 172.30.0.120 | 514 | Medium | 20 |
| 14 | RDP | NW-RDP-001 | 172.30.0.130 | 3389 | Medium | 20 |

**Total: 230 points**

## Network

The Docker laboratory uses:

```text
172.30.0.0/24


The training portal is:

172.30.0.10

The target services occupy:

172.30.0.20 - 172.30.0.160
Training Portal

Start the lab and access:

http://localhost:8081

The portal provides:

Enumeration questions
Difficulty information
Trophy validation
Hints
Progress tracking
Completion scoring

Progress:

http://localhost:8081/progress
Requirements

Recommended platform:

Kali Linux
Docker
Docker Compose
Git

Recommended enumeration tools:

nmap
smbclient
curl
ftp
dig
ldapsearch
snmpwalk
snmpget
nc
openssl

Install common tools on Kali:

sudo apt update
sudo apt install -y nmap smbclient curl ftp dnsutils ldap-utils snmp netcat-openbsd openssl
Installation

Clone the repository:

git clone https://github.com/JCl3m3nts/crest-lab-lite.git
cd crest-lab-lite

Build:

sudo docker compose build

Start:

sudo docker compose up -d

Check:

sudo docker compose ps

Open:

http://localhost:8081
Host Ports
Service	Host Port
SMB	139 / 445
FTP	21
HTTP	8080
SSH	2222
DNS	53
LDAP	389
SNMP	161 UDP
Telnet	23
Finger	79
RSH	514
RDP	3389
SMTP	25
POP3	110
IMAPS	993
Portal	8081
Enumeration Workflow

The intended workflow is reconnaissance first, followed by targeted enumeration.

Service discovery
nmap -Pn -sV 172.30.0.0/24

Or scan the known service ports:

nmap -Pn -sV \
-p 21,22,23,25,79,80,110,139,389,445,514,993,3389 \
172.30.0.20 \
172.30.0.30 \
172.30.0.40 \
172.30.0.50 \
172.30.0.60 \
172.30.0.70 \
172.30.0.90 \
172.30.0.100 \
172.30.0.110 \
172.30.0.120 \
172.30.0.130 \
172.30.0.140 \
172.30.0.150 \
172.30.0.160
SMB
smbclient -L //172.30.0.20 -N
FTP
ftp 172.30.0.30
HTTP
curl -i http://172.30.0.40/
SSH
nc -nv 172.30.0.50 22
DNS
dig @172.30.0.60 northwind.local SOA
dig @172.30.0.60 northwind.local AXFR
LDAP
ldapsearch -x \
-H ldap://172.30.0.70:389 \
-D "cn=admin,dc=northwind,dc=local" \
-w 'Password123!' \
-b "dc=northwind,dc=local"
SNMP
snmpwalk -v2c -c public 172.30.0.90
Telnet
nc -nv 172.30.0.100 23
Finger
printf "\r\n" | nc 172.30.0.110 79
RSH
nc -nv 172.30.0.120 514
RDP
nc -nv 172.30.0.130 3389
SMTP
nc -nv 172.30.0.140 25
POP3
nc -nv 172.30.0.150 110
IMAPS
openssl s_client \
-connect 172.30.0.160:993 \
-servername imap.northwind.local
Question Objectives

The 14 challenges require enumeration of:

SMB public share and trophy
Anonymous FTP
HTTP web content and hidden location
SSH service information
DNS records and zone information
SNMP information
Telnet service
Finger information
LDAP directory information
SMTP service
POP3 service
IMAPS/TLS service
RSH service and configuration
RDP service

The objective is to discover the required information through enumeration rather than simply reading the database.

Database

The training database is:

data/crest.db

Inspect it:

sqlite3 data/crest.db

Example:

SELECT id, category, difficulty, points
FROM questions
ORDER BY id;

Expected database state:

14 questions
14 trophies
230 total points
Progress

The portal tracks completed questions.

Visit:

http://localhost:8081/progress
Docker Management

Stop the lab:

sudo docker compose down

Start again:

sudo docker compose up -d

Rebuild:

sudo docker compose build
sudo docker compose up -d

Complete rebuild:

sudo docker compose down
sudo docker compose build --no-cache
sudo docker compose up -d
Troubleshooting

Check containers:

sudo docker compose ps

Check the lab network:

sudo docker network inspect crest-lab-lite_crest-network

Check the portal:

curl -i http://localhost:8081/

Check Flask errors:

sudo docker exec crest-lab \
tail -100 /var/log/supervisor/crest-web-stderr---*.log

Check service logs:

sudo docker compose logs --tail=100
Validation

A successful deployment should show:

14 target services
14 questions
14 trophies
230 points
Portal HTTP 200

The final service validation should identify:

SMB      172.30.0.20
FTP      172.30.0.30
HTTP     172.30.0.40
SSH      172.30.0.50
DNS      172.30.0.60
LDAP     172.30.0.70
SNMP     172.30.0.90
TELNET   172.30.0.100
FINGER   172.30.0.110
RSH      172.30.0.120
RDP      172.30.0.130
SMTP     172.30.0.140
POP3     172.30.0.150
IMAPS    172.30.0.160
Project Structure
crest-lab-lite/
├── data/
│   ├── crest.db
│   └── init_db.py
├── portal/
│   ├── app/
│   └── requirements.txt
├── services/
│   ├── smb/
│   ├── ftp/
│   ├── http/
│   ├── ssh/
│   ├── dns/
│   ├── ldap/
│   ├── snmp/
│   ├── telnet/
│   ├── finger/
│   ├── rsh/
│   ├── rdp/
│   ├── smtp/
│   ├── pop3/
│   └── imaps/
├── docker-compose.yml
├── Dockerfile
├── supervisord.conf
├── README.md
└── userguide.txt
Learning Outcomes

CREST-Lab Lite provides practical experience with:

Network reconnaissance
TCP and UDP service discovery
Service version detection
SMB enumeration
FTP enumeration
Web enumeration
SSH identification
DNS enumeration
LDAP enumeration
SNMP enumeration
Legacy protocol identification
SMTP enumeration
POP3 enumeration
IMAPS and TLS inspection
RSH enumeration
RDP identification
Evidence gathering
Structured penetration-testing methodology
Disclaimer

This project is intentionally designed as a controlled cybersecurity training environment.

Several services use insecure or legacy protocols by design.

Only use this project on systems and networks that you own or have explicit permission to test.
