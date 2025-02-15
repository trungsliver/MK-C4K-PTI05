import json

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address
        }

    @staticmethod
    def from_dict(data):
        return Contact(data["name"], data["phone"], data["email"], data["address"])

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def edit_contact(self, index, contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = contact

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json_contacts = [contact.to_dict() for contact in self.contacts]
            json.dump(json_contacts, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                json_contacts = json.load(file)
                self.contacts = [Contact.from_dict(contact) for contact in json_contacts]
        except FileNotFoundError:
            self.contacts = []