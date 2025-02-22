import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt6.uic import loadUi
from oop import AuthManager, Calculator

class LoginDialog(QDialog):
    def __init__(self, auth_manager):
        super().__init__()
        loadUi("login.ui", self)
        self.auth_manager = auth_manager
        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.show_register_dialog)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if self.auth_manager.login(username, password):
            self.accept()  # Close dialog and return QDialog.Accepted
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password")

    def show_register_dialog(self):
        register_dialog = RegisterDialog(self.auth_manager)
        register_dialog.exec()

class RegisterDialog(QDialog):
    def __init__(self, auth_manager):
        super().__init__()
        loadUi("register.ui", self)
        self.auth_manager = auth_manager
        self.register_button.clicked.connect(self.register)

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if self.auth_manager.register(username, password):
            QMessageBox.information(self, "Success", "Registration successful!")
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Username already exists")

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("calculator.ui", self)
        self.auth_manager = AuthManager()
        self.calculator = Calculator()
        self.current_input = ""
        self.setup_connections()

        # Load history
        self.calculator.load_history()
        self.update_history_list()

        # Show login dialog
        self.show_login_dialog()

    def show_login_dialog(self):
        login_dialog = LoginDialog(self.auth_manager)
        if login_dialog.exec() != QDialog.DialogCode.Accepted:
            sys.exit()  # Close app if login is not successful

    def setup_connections(self):
        # Kết nối các nút số và phép tính (giữ nguyên như trước)
        self.btn_0.clicked.connect(lambda: self.add_to_input("0"))
        self.btn_1.clicked.connect(lambda: self.add_to_input("1"))
        self.btn_2.clicked.connect(lambda: self.add_to_input("2"))
        self.btn_3.clicked.connect(lambda: self.add_to_input("3"))
        self.btn_4.clicked.connect(lambda: self.add_to_input("4"))
        self.btn_5.clicked.connect(lambda: self.add_to_input("5"))
        self.btn_6.clicked.connect(lambda: self.add_to_input("6"))
        self.btn_7.clicked.connect(lambda: self.add_to_input("7"))
        self.btn_8.clicked.connect(lambda: self.add_to_input("8"))
        self.btn_9.clicked.connect(lambda: self.add_to_input("9"))
        self.btn_dot.clicked.connect(lambda: self.add_to_input("."))
        self.btn_add.clicked.connect(lambda: self.add_to_input("+"))
        self.btn_subtract.clicked.connect(lambda: self.add_to_input("-"))
        self.btn_multiply.clicked.connect(lambda: self.add_to_input("*"))
        self.btn_divide.clicked.connect(lambda: self.add_to_input("/"))
        self.btn_equals.clicked.connect(self.calculate_result)
        self.btn_clear.clicked.connect(self.clear_input)
        self.btn_delete.clicked.connect(self.delete_last)

        # Kết nối nút xóa lịch sử
        self.btn_clear_history.clicked.connect(self.clear_history)

    def add_to_input(self, value):
        self.current_input += value
        self.display.setText(self.current_input)

    def clear_input(self):
        self.current_input = ""
        self.display.clear()

    def delete_last(self):
        self.current_input = self.current_input[:-1]
        self.display.setText(self.current_input)

    def calculate_result(self):
        try:
            result = str(eval(self.current_input))
            self.display.setText(result)
            self.calculator.add_to_history(self.current_input, result)
            self.calculator.save_history()
            self.current_input = result
            self.update_history_list()  # Cập nhật lịch sử sau mỗi phép tính
        except Exception as e:
            QMessageBox.warning(self, "Error", "Invalid expression")

    def update_history_list(self):
        self.history_list.clear()
        for entry in self.calculator.history:
            self.history_list.addItem(f"{entry['expression']} = {entry['result']}")

    def clear_history(self):
        self.calculator.clear_history()
        self.update_history_list()  # Cập nhật giao diện sau khi xóa lịch sử
        QMessageBox.information(self, "Success", "History cleared!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())