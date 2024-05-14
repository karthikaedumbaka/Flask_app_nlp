import json
import os


class Database:
    def insert(self, name, email, password):
        # Check if the file exists and is not empty
        if os.path.exists("users.json") and os.path.getsize("users.json") > 0:
            with open("users.json", "r") as f:
                users = json.load(f)
        else:
            users = {}

        if email in users:
            return False
        else:
            users[email] = [name, password]

        with open("users.json", "w") as f:
            json.dump(users, f)
        return True

    def search(self, email, password):
        if os.path.exists("users.json") and os.path.getsize("users.json") > 0:
            with open("users.json", "r") as f:
                users = json.load(f)
        else:
            users = {}

        if email in users and users[email][1] == password:
            return True
        else:
            return False

