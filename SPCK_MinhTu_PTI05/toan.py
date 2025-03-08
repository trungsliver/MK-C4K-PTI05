# Form implementation generated from reading ui file 'toan.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        MainWindow.setStyleSheet("background-color: rgba(215, 215, 217, 1);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.back_toan = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_toan.setGeometry(QtCore.QRect(40, 30, 121, 41))
        self.back_toan.setStyleSheet("background-color: rgba(217, 144, 102, 1);\n"
"border-radius: 20px;")
        self.back_toan.setObjectName("back_toan")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 80, 500, 120))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(217, 144, 102, 1);\n"
"border-radius: 20px;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.cauhoi = QtWidgets.QLabel(parent=self.centralwidget)
        self.cauhoi.setGeometry(QtCore.QRect(225, 250, 550, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cauhoi.setFont(font)
        self.cauhoi.setStyleSheet("background-color: rgba(217, 144, 102, 1);\n"
"border-radius: 20px;")
        self.cauhoi.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cauhoi.setObjectName("cauhoi")
        self.play_toan = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.play_toan.setGeometry(QtCore.QRect(150, 360, 700, 90))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.play_toan.setFont(font)
        self.play_toan.setStyleSheet("background-color: rgba(76, 100, 115, 0.5);")
        self.play_toan.setInputMask("")
        self.play_toan.setText("")
        self.play_toan.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.play_toan.setObjectName("play_toan")
        self.check_toan = QtWidgets.QPushButton(parent=self.centralwidget)
        self.check_toan.setGeometry(QtCore.QRect(325, 500, 350, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.check_toan.setFont(font)
        self.check_toan.setStyleSheet("background-color: rgba(217, 144, 102, 1);\n"
"border-radius: 20px;")
        self.check_toan.setObjectName("check_toan")
        self.start = QtWidgets.QPushButton(parent=self.centralwidget)
        self.start.setGeometry(QtCore.QRect(325, 620, 350, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.start.setFont(font)
        self.start.setStyleSheet("background-color: rgba(217, 144, 102, 1);\n"
"border-radius: 20px;")
        self.start.setObjectName("start")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.back_toan.setText(_translate("MainWindow", "BACK"))
        self.label.setText(_translate("MainWindow", "Thiên tài toán học"))
        self.cauhoi.setText(_translate("MainWindow", "Câu Hỏi Ở Đây"))
        self.play_toan.setPlaceholderText(_translate("MainWindow", "Câu Trả Lời"))
        self.check_toan.setText(_translate("MainWindow", "CHECK"))
        self.start.setText(_translate("MainWindow", "Bắt Đầu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())



