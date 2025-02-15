import sys
import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from app_ui import Ui_ContactManager
from oop import Contact, User

class ContactManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ContactManager()
        self.ui.setupUi(self)
        
        # Kết nối các nút với hàm xử lý
        self.ui.submitLoginButton.clicked.connect(self.handle_login)
        self.ui.submitSignupButton.clicked.connect(self.handle_signup)
        self.ui.addContactButton.clicked.connect(self.add_contact)
        self.ui.deleteContactButton.clicked.connect(self.delete_contact)
        # self.ui.loadContactsButton.clicked.connect(self.load_contacts)
        
        self.current_user = None
    
    def handle_login(self):
        username = self.ui.usernameInput.text()
        password = self.ui.passwordInput.text()
        
        if User.login(username, password):
            self.current_user = username
            QMessageBox.information(self, "Success", "Login Successful!")
            self.load_contacts()
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password!")
    
    def handle_signup(self):
        username = self.ui.usernameInput.text()
        password = self.ui.passwordInput.text()
        
        if User.register(username, password):
            QMessageBox.information(self, "Success", "Account Created!")
        else:
            QMessageBox.warning(self, "Error", "Username already exists!")
    
    def add_contact(self):
        if not self.current_user:
            QMessageBox.warning(self, "Error", "Please login first!")
            return
        
        name = self.ui.nameInput.text()
        phone = self.ui.phoneInput.text()
        email = self.ui.emailInput.text()
        address = self.ui.addressInput.text()
        
        if Contact.add_contact(self.current_user, name, phone, email, address):
            QMessageBox.information(self, "Success", "Contact Added!")
            self.load_contacts()
        else:
            QMessageBox.warning(self, "Error", "Contact already exists!")
    
    def delete_contact(self):
        if not self.current_user:
            QMessageBox.warning(self, "Error", "Please login first!")
            return
        
        name = self.ui.nameInput.text()
        if Contact.delete_contact(self.current_user, name):
            QMessageBox.information(self, "Success", "Contact Deleted!")
            self.load_contacts()
        else:
            QMessageBox.warning(self, "Error", "Contact not found!")
    
    def load_contacts(self):
        if not self.current_user:
            QMessageBox.warning(self, "Error", "Please login first!")
            return
        
        contacts = Contact.get_contacts(self.current_user)
        self.ui.contactTable.setRowCount(len(contacts))
        for row, contact in enumerate(contacts):
            self.ui.contactTable.setItem(row, 0, QTableWidgetItem(contact["name"]))
            self.ui.contactTable.setItem(row, 1, QTableWidgetItem(contact["phone"]))
            self.ui.contactTable.setItem(row, 2, QTableWidgetItem(contact["email"]))
            self.ui.contactTable.setItem(row, 3, QTableWidgetItem(contact["address"]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContactManager()
    window.show()
    sys.exit(app.exec())
