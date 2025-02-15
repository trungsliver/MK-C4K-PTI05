import os
import json
from PyQt6 import uic, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Lessons/SPCK_notes/notes_manager.ui', self)

        # Liên kết các nút với hành động
        self.notesButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.notesPage))
        self.loginButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.loginPage))
        self.signupButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.signupPage))

        self.submitSignupButton.clicked.connect(self.handle_signup)
        self.submitLoginButton.clicked.connect(self.handle_login)
        self.saveButton.clicked.connect(self.save_note)
        self.loadButton.clicked.connect(self.load_note)

        # File lưu trữ thông tin
        self.users_file = 'Lessons/SPCK_notes/users.json'
        self.notes_file = 'Lessons/SPCK_notes/notes.json'
        self.ensure_files()

        # Biến lưu trạng thái người dùng
        self.current_user = None

    def ensure_files(self):
        """Tạo file users.json và notes.json nếu chưa tồn tại."""
        if not os.path.exists(self.users_file):
            with open(self.users_file, 'w') as file:
                json.dump({}, file)

        if not os.path.exists(self.notes_file):
            with open(self.notes_file, 'w') as file:
                json.dump({}, file)

    def read_file(self, filename):
        """Đọc dữ liệu từ file JSON."""
        with open(filename, 'r') as file:
            return json.load(file)

    def write_file(self, filename, data):
        """Ghi dữ liệu vào file JSON."""
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def handle_signup(self):
        """Xử lý đăng ký người dùng."""
        username = self.signupUsernameInput.text().strip()
        password = self.signupPasswordInput.text().strip()

        if not username or not password:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Tên đăng nhập và mật khẩu không được để trống!")
            return

        users = self.read_file(self.users_file)
        if username in users:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Tên đăng nhập đã tồn tại!")
            return

        # Lưu thông tin người dùng
        users[username] = password
        self.write_file(self.users_file, users)

        QtWidgets.QMessageBox.information(self, "Thành công", "Đăng ký thành công!")
        self.signupUsernameInput.clear()
        self.signupPasswordInput.clear()
        self.stackedWidget.setCurrentWidget(self.loginPage)

    def handle_login(self):
        """Xử lý đăng nhập người dùng."""
        username = self.usernameInput.text().strip()
        password = self.passwordInput.text().strip()

        if not username or not password:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Tên đăng nhập và mật khẩu không được để trống!")
            return

        users = self.read_file(self.users_file)
        if username in users and users[username] == password:
            QtWidgets.QMessageBox.information(self, "Thành công", f"Chào mừng {username}!")
            self.current_user = username
            self.usernameInput.clear()
            self.passwordInput.clear()
            self.stackedWidget.setCurrentWidget(self.notesPage)
        else:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Tên đăng nhập hoặc mật khẩu không chính xác!")

    def save_note(self):
        """Lưu ghi chú hiện tại của người dùng."""
        if not self.current_user:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Bạn cần đăng nhập để lưu ghi chú!")
            return

        note_content = self.noteEditor.toPlainText().strip()
        if not note_content:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Ghi chú không được để trống!")
            return

        notes = self.read_file(self.notes_file)
        notes[self.current_user] = note_content
        self.write_file(self.notes_file, notes)

        QtWidgets.QMessageBox.information(self, "Thành công", "Ghi chú đã được lưu!")

    def load_note(self):
        """Tải ghi chú của người dùng hiện tại."""
        if not self.current_user:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Bạn cần đăng nhập để tải ghi chú!")
            return

        notes = self.read_file(self.notes_file)
        note_content = notes.get(self.current_user, "")
        self.noteEditor.setText(note_content)
        QtWidgets.QMessageBox.information(self, "Thành công", "Ghi chú đã được tải!")

app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec()
