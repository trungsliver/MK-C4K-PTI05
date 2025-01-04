# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 50, 300, 100))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Normal ExtraBold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_username = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_username.setGeometry(QtCore.QRect(220, 190, 350, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Normal")
        font.setPointSize(12)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setStyleSheet("padding-left: 5px;")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(220, 280, 350, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Normal")
        font.setPointSize(12)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("padding-left: 5px;")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.btn_signup = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_signup.setGeometry(QtCore.QRect(310, 390, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Normal ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_signup.setFont(font)
        self.btn_signup.setObjectName("btn_signup")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.label.setText(_translate("MainWindow", "SIGN UP"))
        self.lineEdit_username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.btn_signup.setText(_translate("MainWindow", "Signup"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
