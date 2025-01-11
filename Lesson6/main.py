import sys, os
from PyQt6 import QtGui, QtWidgets, QtCore
import login, signup, oop

# QApplication: quản lý phần giao diện ứng dụng
# QMainWindow: tạo cửa sổ ứng dụng chính

#xu ly
ui = ''
app = QtWidgets.QApplication(sys.argv) 
MainWindow = QtWidgets.QMainWindow()
dtb = oop.UserDatabase()

def homeUi():
    global ui
    ui = signup.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_signup.clicked.connect(signup_check)
    msg_box('test',f'{os.getcwd()}')
    MainWindow.show()

def login_w():
    global ui
    ui = login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_login.clicked.connect(login_check)
    MainWindow.show()

def signup_check():
    check = True
    username = ui.lineEdit_username.text().strip()
    password = ui.lineEdit_password.text().strip()
    # Thiếu thông tin
    if username == '' or password == '':
        check = False
        msg_box('Signup fail', 'Missing information!')
    # Pass và confirm không khớp
    # elif password != confirm:
    #     check = False
    #     msg_box('Signup fail', 'Password and confirm password are not match!')
    # Đã tồn tại username trong danh sách users
    else:
        check_user = dtb.find_player_by_name(username)
        if check_user == True:
            check = False
            msg_box('Signup fail', 'Username already exists!')
    
    # Kiểm tra xem có đang ký thành công không
    if check == True:
        # Add tài khoản mới vào danh sách users
        dtb.add_user(username, password)
        msg_box('Signup success', 'Signup success!')
        login_w()

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

def login_check():
    check = False
    username = ui.lineEdit_username.text().strip()
    password = ui.lineEdit_password.text().strip()
    # Kiểm tra 
    check = dtb.check_login(username, password)
    
    if check == True:
        msg_box('Login success', 'Welcome to my app !!!')
        homeUi()
    else:
        msg_box('Login fail', 'Username or password is incorrect!')
#Run app
homeUi()

sys.exit(app.exec())


# Lưu ý: chuột phải vào folder chứa 2 file này, chọn Open .... terminal
# Câu lệnh convert ui: pyuic6 -x login.ui -o login.py
# Câu lệnh convert ui: pyuic6 -x signup.ui -o signup.py
# Câu lệnh convert qrc: pyside6-rcc img.qrc -o img_rc.py