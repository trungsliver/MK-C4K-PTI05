# Form implementation generated from reading ui file 'zzui_solsrng.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 350)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Roller_Label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Roller_Label.setGeometry(QtCore.QRect(140, 20, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Roller_Label.setFont(font)
        self.Roller_Label.setObjectName("Roller_Label")
        self.Text_Label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Text_Label.setGeometry(QtCore.QRect(32, 110, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Text_Label.setFont(font)
        self.Text_Label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Text_Label.setObjectName("Text_Label")
        self.Rarity_Label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Rarity_Label.setGeometry(QtCore.QRect(33, 140, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Rarity_Label.setFont(font)
        self.Rarity_Label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Rarity_Label.setObjectName("Rarity_Label")
        self.Earn_Label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Earn_Label.setGeometry(QtCore.QRect(7, 315, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Earn_Label.setFont(font)
        self.Earn_Label.setStyleSheet("color: rgb(0, 177, 0);")
        self.Earn_Label.setObjectName("Earn_Label")
        self.Price_Rollbox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.Price_Rollbox.setGeometry(QtCore.QRect(100, 250, 42, 22))
        self.Price_Rollbox.setMinimum(1)
        self.Price_Rollbox.setMaximum(999999999)
        self.Price_Rollbox.setObjectName("Price_Rollbox")
        self.Roll_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Roll_Button.setGeometry(QtCore.QRect(150, 240, 81, 41))
        self.Roll_Button.setObjectName("Roll_Button")
        self.RTDB_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.RTDB_Button.setGeometry(QtCore.QRect(240, 10, 111, 21))
        self.RTDB_Button.setFlat(True)
        self.RTDB_Button.setObjectName("RTDB_Button")
        self.Error_Label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Error_Label.setGeometry(QtCore.QRect(20, 293, 311, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Error_Label.setFont(font)
        self.Error_Label.setStyleSheet("color: rgb(255, 0, 0);")
        self.Error_Label.setText("")
        self.Error_Label.setObjectName("Error_Label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Roller (bootleg Sol\'s RNG)"))
        self.Roller_Label.setText(_translate("MainWindow", "Roller"))
        self.Text_Label.setText(_translate("MainWindow", "Text"))
        self.Rarity_Label.setText(_translate("MainWindow", "Rarity"))
        self.Earn_Label.setText(_translate("MainWindow", "Earn amount"))
        self.Roll_Button.setText(_translate("MainWindow", "Roll"))
        self.RTDB_Button.setText(_translate("MainWindow", "Return to dashboard"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
