# Form implementation generated from reading ui file 'signin.ui'
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
        MainWindow.setStyleSheet("background-color: rgba(215, 215, 217, 1);\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_login = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_login.setGeometry(QtCore.QRect(425, 670, 150, 40))
        self.pushButton_login.setStyleSheet("background-color: rgba(217, 144, 102, 1)\n"
"")
        self.pushButton_login.setObjectName("pushButton_login")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 290, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(56, 77, 89, 1);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 440, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(56, 77, 89, 1);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(80, 500, 700, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("background-color: rgba(76, 100, 115, 0.5);")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 40, 600, 150))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgba(217, 144, 102, 1);\n"
"border-radius: 20px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_email = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(80, 350, 700, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setStyleSheet("background-color: rgba(76, 100, 115, 0.5);")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.next_login = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next_login.setGeometry(QtCore.QRect(110, 670, 231, 41))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.next_login.setFont(font)
        self.next_login.setStyleSheet("color: blue")
        self.next_login.setObjectName("next_login")
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
        self.pushButton_login.setText(_translate("MainWindow", "login"))
        self.label_3.setText(_translate("MainWindow", "Email:"))
        self.label_4.setText(_translate("MainWindow", "Password:"))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow", "password"))
        self.pushButton_2.setText(_translate("MainWindow", "LOGIN"))
        self.lineEdit_email.setPlaceholderText(_translate("MainWindow", "input email"))
        self.next_login.setText(_translate("MainWindow", "I haven\'t an account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
