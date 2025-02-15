import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import pyqtSlot
from contact_manager import Ui_MainWindow
from oop import User, Contact, ContactManager

class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.contact_manager = ContactManager()
        self.ui.btnAddContact.clicked.connect(self.add_contact)
        self.ui.btnEditContact.clicked.connect(self.edit_contact)
        self.ui.btnDeleteContact.clicked.connect(self.delete_contact)
        self.ui.btnSaveContacts.clicked.connect(self.save_contacts)
        self.ui.btnLoadContacts.clicked.connect(self.load_contacts)

    @pyqtSlot()
    def add_contact(self):
        name = self.ui.txtName.text()
        phone = self.ui.txtPhone.text()
        email = self.ui.txtEmail.text()
        address = self.ui.txtAddress.text()
        if name and phone and email and address:
            contact = Contact(name, phone, email, address)
            self.contact_manager.add_contact(contact)
            self.clear_fields()
            self.update_contact_list()
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đủ thông tin liên hệ.")

    @pyqtSlot()
    def edit_contact(self):
        index = self.ui.lstContacts.currentRow()
        name = self.ui.txtName.text()
        phone = self.ui.txtPhone.text()
        email = self.ui.txtEmail.text()
        address = self.ui.txtAddress.text()
        if 0 <= index < len(self.contact_manager.contacts):
            contact = Contact(name, phone, email, address)
            self.contact_manager.edit_contact(index, contact)
            self.clear_fields()
            self.update_contact_list()
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một liên hệ để chỉnh sửa.")

    @pyqtSlot()
    def delete_contact(self):
        index = self.ui.lstContacts.currentRow()
        if 0 <= index < len(self.contact_manager.contacts):
            self.contact_manager.delete_contact(index)
            self.update_contact_list()
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một liên hệ để xóa.")

    @pyqtSlot()
    def save_contacts(self):
        self.contact_manager.save_to_file('Lessons/SPCK_Contact/contacts.json')
        QMessageBox.information(self, "Thành công", "Danh bạ đã được lưu.")

    @pyqtSlot()
    def load_contacts(self):
        self.contact_manager.load_from_file('Lessons/SPCK_Contact/contacts.json')
        self.update_contact_list()

    def clear_fields(self):
        self.ui.txtName.clear()
        self.ui.txtPhone.clear()
        self.ui.txtEmail.clear()
        self.ui.txtAddress.clear()

    def update_contact_list(self):
        self.ui.lstContacts.clear()
        for contact in self.contact_manager.contacts:
            self.ui.lstContacts.addItem(f"{contact.name} - {contact.phone}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())