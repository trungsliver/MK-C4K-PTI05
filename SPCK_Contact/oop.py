import json, os


# Xem đường dẫn hiện tại
# print(os.getcwd()) 
USER_FILE = "Lessons/SPCK_Contact/users.json"
CONTACT_FILE = "Lessons/SPCK_Contact/contacts.json"

class User:
    @staticmethod
    def load_users():
        try:
            with open(USER_FILE, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
    
    @staticmethod
    def save_users(users):
        with open(USER_FILE, "w") as file:
            json.dump(users, file, indent=4)
    
    @classmethod
    def register(cls, username, password):
        users = cls.load_users()
        if username in users:
            return False
        users[username] = password
        cls.save_users(users)
        return True
    
    @classmethod
    def login(cls, username, password):
        users = cls.load_users()
        return users.get(username) == password

class Contact:
    @staticmethod
    def load_contacts():
        try:
            with open(CONTACT_FILE, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
    
    @staticmethod
    def save_contacts(contacts):
        with open(CONTACT_FILE, "w") as file:
            json.dump(contacts, file, indent=4)
    
    @classmethod
    def add_contact(cls, username, name, phone, email, address):
        contacts = cls.load_contacts()
        if username not in contacts:
            contacts[username] = []
        for contact in contacts[username]:
            if contact["name"] == name:
                return False
        contacts[username].append({"name": name, "phone": phone, "email": email, "address": address})
        cls.save_contacts(contacts)
        return True
    
    @classmethod
    def delete_contact(cls, username, name):
        contacts = cls.load_contacts()
        if username in contacts:
            contacts[username] = [c for c in contacts[username] if c["name"] != name]
            cls.save_contacts(contacts)
            return True
        return False
    
    @classmethod
    def get_contacts(cls, username):
        contacts = cls.load_contacts()
        return contacts.get(username, [])
