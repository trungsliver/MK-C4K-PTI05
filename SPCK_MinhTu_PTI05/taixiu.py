

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        font = QtGui.QFont()
        font.setUnderline(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("""
            background-color: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 #8B0000,
                stop: 1 #B22222
            );
        """)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Nút Rút Bài
        self.btn_draw = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_draw.setGeometry(QtCore.QRect(200, 100, 200, 50))
        self.setup_button(self.btn_draw, "Rút Bài")

        # Nút Dừng
        self.btn_stop = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(400, 100, 200, 50))
        self.setup_button(self.btn_stop, "Dừng")

        # Nút Chơi Lại
        self.btn_reset = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(600, 100, 200, 50))
        self.setup_button(self.btn_reset, "Chơi Lại")

        # Nút Quay về
        self.btn_back = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(10, 10, 150, 50))
        self.setup_button(self.btn_back, "Quay về")

        # Khung hiển thị lá bài và điểm số của người chơi
        self.create_side_frame("Người Chơi", QtCore.QRect(50, 200, 400, 500), "player")
        # Khung hiển thị lá bài và điểm số của bot
        self.create_side_frame("Bot", QtCore.QRect(550, 200, 400, 500), "bot")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setup_button(self, button, text):
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        button.setFont(font)
        button.setText(text)
        button.setStyleSheet("""
            QPushButton {
                background-color: #FF4500;
                color: white;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #FF6347;
            }
        """)

    def create_side_frame(self, title, geometry, player_type):
        frame = QtWidgets.QFrame(parent=self.centralwidget)
        frame.setGeometry(geometry)
        frame.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.12);
                border: 2px solid #FF6347;
                border-radius: 15px;
            }
        """)

        label_title = QtWidgets.QLabel(parent=frame)
        label_title.setGeometry(QtCore.QRect(0, 10, geometry.width(), 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        label_title.setFont(font)
        label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        label_title.setStyleSheet("color: white;")
        label_title.setText(title)

        # Hiển thị lá bài
        if player_type == "player":
            self.card_display_player = QtWidgets.QTextEdit(parent=frame)
            self.card_display_player.setGeometry(QtCore.QRect(20, 60, geometry.width() - 40, 150))
            self.card_display_player.setPlaceholderText(f"Lá bài của {title.lower()} sẽ hiển thị ở đây...")
            self.card_display_player.setReadOnly(True)
            self.card_display_player.setStyleSheet("""
                QTextEdit {
                    background-color: rgba(255, 255, 255, 0.9);
                    color: black;
                    border-radius: 10px;
                    font-size: 16px;
                    padding: 8px;
                }
            """)
            # Hiển thị điểm số
            self.score_label_player = QtWidgets.QLabel(parent=frame)
            self.score_label_player.setGeometry(QtCore.QRect(20, 220, geometry.width() - 40, 30))
            self.score_label_player.setStyleSheet("color: white; font-size: 18px;")
            self.score_label_player.setText("Điểm: 0")
        else:
            self.card_display_bot = QtWidgets.QTextEdit(parent=frame)
            self.card_display_bot.setGeometry(QtCore.QRect(20, 60, geometry.width() - 40, 150))
            self.card_display_bot.setPlaceholderText(f"Lá bài của {title.lower()} sẽ hiển thị ở đây...")
            self.card_display_bot.setReadOnly(True)
            self.card_display_bot.setStyleSheet("""
                QTextEdit {
                    background-color: rgba(255, 255, 255, 0.9);
                    color: black;
                    border-radius: 10px;
                    font-size: 16px;
                    padding: 8px;
                }
            """)
            # Hiển thị điểm số
            self.score_label_bot = QtWidgets.QLabel(parent=frame)
            self.score_label_bot.setGeometry(QtCore.QRect(20, 220, geometry.width() - 40, 30))
            self.score_label_bot.setStyleSheet("color: white; font-size: 18px;")
            self.score_label_bot.setText("Điểm: 0")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "🎴 Xì Dách 🎴"))