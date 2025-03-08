import sys, image_rc, login, register
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QApplication, QWidget
from PyQt6 import QtGui, QtWidgets,uic
from PyQt6.QtCore import pyqtSlot
from contact_manager import Ui_MainWindow
from oop import User, Contact, ContactManager
from register import Ui_RegisterWindow
from login import Ui_LoginWindow
 
current_account = ''
users = ['admin:admin']

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('register.ui', self)
        self.pb_signup.clicked.connect(self.signup_check)
        self.pb_signup_2.clicked.connect(self.switch_login)

    def signup_check(self):
        check = True
        username = self.txtSUsername.text().strip()
        password = self.txtSPass.text().strip()
        confirm = self.txtCfpass.text().strip()
        #thiếu thông tin
        if username == '' or username == '' or password == '' or confirm == '':
            check = False
            msg_box('Signup', 'Missing information!')
        #pass và cfpass ko khớp
        elif password !=confirm:
            check = False
            msg_box('Signup', 'Passwords did not match!')
        #đã tồn tại username trong danh sách users
        else:
            for user in users:
                stored_username, stored_password = user.split(':',1)
                if username == stored_username:
                    check = False
                    msg_box('Signup', 'Username already exists!')
    # Kiểm tra xem có đang ký thành công không
        if check == True:
            # Add tài khoản mới vào danh sách users
            new_acc = username + ':' + password
            users.append(new_acc)
            msg_box('Signup', 'Signup success!')
            print(users)
            switch_window(Login())

    def switch_login(self):
        switch_window(Login())

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('login.ui', self)
        self.pb_login.clicked.connect(self.login_check)
        self.pb_signup_3.clicked.connect(self.switch_register)

    def switch_register(self):
        switch_window(Register())
        
    def login_check(self):
        check = False
        username = self.txtLUsername.text().strip()
        password = self.txtLPass.text().strip()
        #check
        for user in users:
            stored_username, stored_password = user.split(':',1)
            if username == stored_username and password == stored_password:
                check = True

        if check == True:
            msg_box("Login",'Welcome!')
            switch_window(MainApp())
        else:
            msg_box('Login', 'Invalid username or password!')

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('contact_manager.ui', self)
        self.contact_manager = ContactManager()
        self.btnAddContact.clicked.connect(self.add_contact)
        self.btnEditContact.clicked.connect(self.edit_contact)
        self.btnDeleteContact.clicked.connect(self.delete_contact)
        self.btnSaveContacts.clicked.connect(self.save_contacts)
        self.btnLoadContacts.clicked.connect(self.load_contacts)

    @pyqtSlot()
    def add_contact(self):
        name = self.txtName.text()
        phone = self.txtPhone.text()
        email = self.txtEmail.text()
        address = self.txtAddress.text()
        if name and phone and email and address:
            contact = Contact(name, phone, email, address)
            self.contact_manager.add_contact(contact)
            self.clear_fields()
            self.update_contact_list()
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đủ thông tin liên hệ.")

    @pyqtSlot()
    def edit_contact(self):
        index = self.lstContacts.currentRow()
        name = self.txtName.text()
        phone = self.txtPhone.text()
        email = self.txtEmail.text()
        address = self.txtAddress.text()
        if 0 <= index < len(self.contact_manager.contacts):
            contact = Contact(name, phone, email, address)
            self.contact_manager.edit_contact(index, contact)
            self.clear_fields()
            self.update_contact_list()
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một liên hệ để chỉnh sửa.")

    @pyqtSlot()
    def delete_contact(self):
        index = self.lstContacts.currentRow()
        if 0 <= index < len(self.contact_manager.contacts):
            self.contact_manager.delete_contact(index)
            self.update_contact_list()
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một liên hệ để xóa.")

    @pyqtSlot()
    def save_contacts(self):
        self.contact_manager.save_to_file('contacts.json')
        QMessageBox.information(self, "Thành công", "Danh bạ đã được lưu.")

    @pyqtSlot()
    def load_contacts(self):
        self.contact_manager.load_from_file('contacts.json')
        self.update_contact_list()

    def clear_fields(self):
        self.txtName.clear()
        self.txtPhone.clear()
        self.txtEmail.clear()
        self.txtAddress.clear()

    def update_contact_list(self):
        self.lstContacts.clear()
        for contact in self.contact_manager.contacts:
            self.lstContacts.addItem(f"{contact.name} - {contact.phone}")

def msg_box(title, content):
    msg = QtWidgets.QMessageBox()
    msg.setStyleSheet("QLabel{min-width: 200px;}"
                          "QLabel{max-width: 200px;}"
                          "QMessageBox{background-color:rgba(35,36,40,255);}"
                          "QPushButton{background-color:rgb(30,95,181);}"
                          "QLabel{color:rgb(255,255,255);}"
                          "QPushButton{color:rgb(255,255,255);}")
    msg.setWindowTitle(title)
    msg.setInformativeText(content)
    msg.exec()

def switch_window(classw):
    global window
    window = classw
    window.show()

app = QApplication(sys.argv)
window = Register()
window.show()
sys.exit(app.exec())

# Câu lệnh convert: pyuic6 -x L6.ui -o L6.py
# Lưu ý: chuột phải vào folder chứa 2 file này, chọn Open .... terminal
# Câu lệnh convert ui: pyuic6 -x lesson6.ui -o lesson6.py
# Câu lệnh convert qrc: pyside6-rcc img.qrc -o img_rc.py