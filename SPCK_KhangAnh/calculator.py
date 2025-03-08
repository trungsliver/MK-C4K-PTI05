from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from oop import User, History

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui_calculator.ui", self)

        self.current_user = None
        self.expression = ""

        # Kết nối các nút
        self.btn_0.clicked.connect(lambda: self.append_number("0"))
        self.btn_1.clicked.connect(lambda: self.append_number("1"))
        self.btn_2.clicked.connect(lambda: self.append_number("2"))
        self.btn_3.clicked.connect(lambda: self.append_number("3"))
        self.btn_4.clicked.connect(lambda: self.append_number("4"))
        self.btn_5.clicked.connect(lambda: self.append_number("5"))
        self.btn_6.clicked.connect(lambda: self.append_number("6"))
        self.btn_7.clicked.connect(lambda: self.append_number("7"))
        self.btn_8.clicked.connect(lambda: self.append_number("8"))
        self.btn_9.clicked.connect(lambda: self.append_number("9"))
        self.btn_add.clicked.connect(lambda: self.append_number("+"))
        self.btn_sub.clicked.connect(lambda: self.append_number("-"))
        self.btn_mul.clicked.connect(lambda: self.append_number("*"))
        self.btn_div.clicked.connect(lambda: self.append_number("/"))
        self.btn_clear.clicked.connect(self.clear_expression)
        self.btn_equal.clicked.connect(self.calculate_result)
        self.btn_login.clicked.connect(self.handle_login)
        self.btn_register.clicked.connect(self.handle_register)
        self.btn_clear_history.clicked.connect(self.clear_history)

    def append_number(self, num):
        self.expression += num
        self.display.setText(self.expression)

    def clear_expression(self):
        self.expression = ""
        self.display.setText("")

    def calculate_result(self):
        try:
            result = str(eval(self.expression))
            self.display.setText(result)
            if self.current_user:
                History.add_record(self.expression, result)
            self.expression = result
        except Exception:
            self.display.setText("Error")
            self.expression = ""

    def handle_login(self):
        username = self.input_username.text()
        password = self.input_password.text()
        if User.login(username, password):
            self.current_user = username
            QMessageBox.information(self, "Thành công", "Đăng nhập thành công!")
        else:
            QMessageBox.warning(self, "Lỗi", "Sai tên đăng nhập hoặc mật khẩu.")

    def handle_register(self):
        username = self.input_username.text()
        password = self.input_password.text()
        if User.register(username, password):
            QMessageBox.information(self, "Thành công", "Đăng ký thành công!")
        else:
            QMessageBox.warning(self, "Lỗi", "Tên đăng nhập đã tồn tại.")

    def clear_history(self):
        if self.current_user:
            History.clear_history()
            QMessageBox.information(self, "Thành công", "Đã xóa lịch sử tính toán.")
