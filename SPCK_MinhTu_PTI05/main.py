import sys
from PyQt6 import QtWidgets, QtCore
import signin 
import signup
import game
import images_rc
import doanso
import toan
import taixiu
import random
import os, json, operator
import oop
from taixiu import Ui_MainWindow

# Biến toàn cục
e = 0
ui = ''
app = QtWidgets.QApplication(sys.argv) 
MainWindow = QtWidgets.QMainWindow()
dtb = oop.accDatabase()
dtb.load_data
ui = None
rd = 0
attempts = 0
d = None

values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
deck = []
pl1, bot = [], []
scpl1, scbot = 0, 0

def create_deck():
    return [f'{value}:{suit}' for suit in suits for value in values]

def get_card_value(value, current_score):
    if value in ['J', 'Q', 'K']:
        return 10
    elif value == 'A':
        return 11 if current_score + 11 <= 21 else 1
    return int(value)

def boc(player):
    global scpl1, scbot, deck
    if not deck:
        deck = create_deck()
    card = random.choice(deck)
    deck.remove(card)
    value, _ = card.split(":")
    if player == 'player':
        pl1.append(card)
        scpl1 += get_card_value(value, scpl1)
    else:
        bot.append(card)
        scbot += get_card_value(value, scbot)

def check_win():
    if scpl1 > 21:
        return "Bạn đã thua!"
    elif scbot > 21 or scpl1 > scbot:
        return "Bạn thắng!"
    elif scpl1 < scbot:
        return "Bạn thua!"
    return "Hòa!"

def player_draw():
    boc('player')
    update_display()
    if scpl1 > 21:
        msg_box("Thua", "Bạn đã quá 21 điểm!")
        player_stand()

def player_stand():
    while scbot < 17:  # Bot tự động rút bài nếu điểm < 17
        boc('bot')
    result = check_win()
    msg_box("Kết Quả", result)
    update_display()

def reset_game():
    global deck, pl1, bot, scpl1, scbot
    deck = create_deck()
    pl1, bot = [], []
    scpl1, scbot = 0, 0
    update_display()

def update_display():
    ui.card_display_player.setPlainText("\n".join(pl1))
    ui.score_label_player.setText(f"Điểm: {scpl1}")
    ui.card_display_bot.setPlainText("\n".join(bot))
    ui.score_label_bot.setText(f"Điểm: {scbot}")

def taixiu_w():
    global ui
    ui = taixiu.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_draw.clicked.connect(player_draw)
    ui.btn_stop.clicked.connect(player_stand)
    ui.btn_reset.clicked.connect(reset_game)
    ui.btn_back.clicked.connect(gameUi)
    reset_game()  # Khởi tạo trò chơi
    MainWindow.show()

def homeUi():
    global ui
    ui = signup.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton_sign_up.clicked.connect(signup_check)
    ui.next_login.clicked.connect(login_w)
    MainWindow.show()

def toan_w():
    global ui, d
    ui = toan.Ui_MainWindow()
    ui.setupUi(MainWindow)
    d = None
    ui.start.clicked.connect(phep_tinh)
    ui.check_toan.clicked.connect(check_toan)
    ui.back_toan.clicked.connect(gameUi)
    MainWindow.show()
    
def login_w():
    global ui
    ui = signin.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton_login.clicked.connect(login_check)
    ui.next_login.clicked.connect(homeUi)
    MainWindow.show()

def gameUi():
    global ui
    ui = game.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.next_doanso.clicked.connect(doanso_w)
    ui.next_toan.clicked.connect(toan_w)
    MainWindow.show()

def toan_w():
    global ui, d
    ui = toan.Ui_MainWindow()
    ui.setupUi(MainWindow)
    d = None
    ui.start.clicked.connect(phep_tinh)
    ui.check_toan.clicked.connect(check_toan)
    ui.back_toan.clicked.connect(gameUi)
    MainWindow.show()

def update_toan_text():
    text_content = ui.play_toan.text()
    if text_content.isdigit() or text_content == "":
        return
    msg_box("Lỗi nhập", "Vui lòng nhập một số nguyên hợp lệ.")
    ui.play_toan.clear()

def check_toan():
    global d, e
    if d is None:
        msg_box("Chưa có phép tính", "Vui lòng nhấn 'Bắt Đầu' để tạo phép tính trước.")
        ui.play_toan.clear()
        return

    try:
        user_number = int(ui.play_toan.text().strip())
    except ValueError:
        msg_box("Lỗi nhập", "Vui lòng nhập một số nguyên hợp lệ.")
        ui.play_toan.clear()
        return

    if user_number == d:
        msg_box("Kết quả đúng", "Bạn đã trả lời đúng!")
        phep_tinh()
        ui.play_toan.clear()
        e += 1
        if e == 5:
            msg_box("Win", "YOU WIN!!!")
    else:
        msg_box("Kết quả sai", f"Kết quả đúng là {d}")
        phep_tinh()
        ui.play_toan.clear()

def phep_tinh():
    global d
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 4)
    if c == 1:
        ui.cauhoi.setText(f'{a} + {b}')
        d = a + b
    elif c == 2:
        ui.cauhoi.setText(f'{a} - {b}')
        d = a - b
    elif c == 3:
        ui.cauhoi.setText(f'{a} x {b}')
        d = a * b
    elif c == 4:
        ui.cauhoi.setText(f'{a} / {b}')
        d = round(a / b)

def doanso_w():
    global ui, rd, attempts
    ui = doanso.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.check.clicked.connect(doanso_check)
    ui.back_doanso.clicked.connect(gameUi)
    ui.play_doanso.textChanged.connect(update_doanso_text)
    MainWindow.show()

    rd = random.randint(1, 50)
    attempts = 0

def update_doanso_text():
    text_content = ui.play_doanso.text()
    if text_content.isdigit() or text_content == "":
        return
    msg_box("Lỗi nhập", "Vui lòng nhập một số nguyên hợp lệ.")
    ui.play_doanso.clear()

def doanso_check():
    global rd, attempts
    try:
        user_number = int(ui.play_doanso.text().strip())
    except ValueError:
        msg_box("Lỗi nhập", "Vui lòng nhập một số nguyên hợp lệ.")
        return
    if user_number == 666:
        taixiu_w()
        return
        
    elif user_number > 51 or user_number < 0:
        ui.goiy.setText("Vui lòng nhập số từ 1-50")
        ui.play_doanso.clear()

    attempts += 1

    if user_number < rd:
        ui.goiy.setText(f"Số cần đoán lớn hơn {user_number}")
        ui.play_doanso.clear()
    elif user_number > rd:
        ui.goiy.setText(f"Số cần đoán nhỏ hơn {user_number}")
        ui.play_doanso.clear()     
    else:
        msg_box("Chúc mừng", f"Bạn đã đoán đúng sau {attempts} lần thử!")
        attempts = 0
        rd = random.randint(1, 50)
        ui.goiy.setText('Gợi Ý Ở Đây')
        ui.play_doanso.clear()

def signup_check():
    global ui
    age = ui.lineEdit_age.text().strip()
    name = ui.lineEdit_name.text().strip()
    email = ui.lineEdit_email.text().strip()
    password = ui.lineEdit_password.text().strip()

    # Kiểm tra các trường thông tin có đầy đủ không
    if not all([name, email, password, age]):
        msg_box('Sigup fail', 'Missing information')
        return

    # Kiểm tra tuổi có hợp lệ không
    try:
        age = int(age)
    except ValueError:
        msg_box("Error", "Please enter a valid integer for age")
        return

    # Kiểm tra nếu tài khoản đã tồn tại
    acc_db = oop.accDatabase()
    acc_db.load_data()

    for acc in acc_db.acc_list:
        if acc.mail == email:
            msg_box("Error", 'account already exists')
            return
    msg_box('Login success', 'Welcome to my app !!!')
            # return
            # Tạo đối tượng mới và thêm vào cơ sở dữ liệu
    new_user = {
                "name": name,
                "mail": email,
                "password": password,
                "age": age,
                "achievements":{
                "first_signup": False,
                "first_login": False,
                "win_toan": False,
                "win_doanso": False,
                "join_xijack": False,
                "win_xijack": False
    }}
    gameUi()

def login_check():
    email = ui.lineEdit_email.text().strip()
    password = ui.lineEdit_password.text().strip()

    # Kiểm tra đăng nhập
    acc_db = oop.accDatabase()
    acc_db.load_data()  # Đảm bảo dữ liệu đã được tải
    check = acc_db.check_login(email, password)
    
    if check:
        msg_box('Login success', 'Welcome to my app !!!')
        gameUi()  # Mở màn hình game sau khi đăng nhập thành công
    else:
        msg_box('Login fail', 'email or password is incorrect!')  # Thông báo lỗi nếu đăng nhập thất bại

def msg_box(title, content):
    msg = QtWidgets.QMessageBox()
    msg.setStyleSheet(
        "QLabel{min-width: 200px;} QLabel{max-width: 200px;}"
        "QMessageBox{background-color:rgba(35,36,40,255);}"
        "QPushButton{background-color:rgb(30,95,181);}"
        "QLabel{color:rgb(255,255,255);} QPushButton{color:rgb(255,255,255);}"
    )
    msg.setWindowTitle(title)
    msg.setInformativeText(content)
    msg.exec()

homeUi()
sys.exit(app.exec())