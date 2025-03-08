import json
import os

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password
        }

class AuthManager:
    def __init__(self, filename="users.json"):
        self.filename = filename
        self.users = self.load_users()

    def load_users(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return []

    def save_users(self):
        with open(self.filename, "w") as file:
            json.dump(self.users, file)

    def register(self, username, password):
        if any(user["username"] == username for user in self.users):
            return False  # Username already exists
        new_user = User(username, password).to_dict()
        self.users.append(new_user)
        self.save_users()
        return True

    def login(self, username, password):
        for user in self.users:
            if user["username"] == username and user["password"] == password:
                return True
        return False

class Calculator:
    def __init__(self):
        self.history = []

    def add_to_history(self, expression, result):
        self.history.append({"expression": expression, "result": result})

    def save_history(self, filename="history.json"):
        with open(filename, "w") as file:
            json.dump(self.history, file)

    def load_history(self, filename="history.json"):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                self.history = json.load(file)

    def clear_history(self, filename="history.json"):
        self.history = []
        if os.path.exists(filename):
            os.remove(filename)