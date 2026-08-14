#!/usr/bin/env python3

import sys
import pwd

request = sys.stdin.read().strip()

users = {
    "analyst": {
        "name": "Sarah Mitchell - IT Support",
        "login": "analyst",
        "office": "Northwind HQ",
        "email": "sarah.mitchell@northwind.local"
    }
}

if request in ("", "analyst"):
    for user in users.values():
        if request == "" or request == user["login"]:
            print(f"Login: {user['login']}")
            print(f"Name: {user['name']}")
            print(f"Office: {user['office']}")
            print(f"Mail: {user['email']}")
            print()
else:
    print(f"finger: {request}: no such user")
