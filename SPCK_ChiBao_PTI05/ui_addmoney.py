# Form implementation generated from reading ui file 'zzui_addmoney.ui'
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
        self.Addmoney_Label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Addmoney_Label.setGeometry(QtCore.QRect(105, 40, 170, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Addmoney_Label.setFont(font)
        self.Addmoney_Label.setObjectName("Addmoney_Label")
        self.RTDB_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.RTDB_Button.setGeometry(QtCore.QRect(240, 10, 111, 21))
        self.RTDB_Button.setFlat(True)
        self.RTDB_Button.setObjectName("RTDB_Button")
        self.Add_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Add_Button.setGeometry(QtCore.QRect(130, 270, 91, 31))
        self.Add_Button.setObjectName("Add_Button")
        self.Money_Line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Money_Line.setGeometry(QtCore.QRect(60, 170, 231, 20))
        self.Money_Line.setObjectName("Money_Line")
        self.Error_Label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Error_Label.setGeometry(QtCore.QRect(20, 230, 311, 16))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Slot Machine"))
        self.Addmoney_Label.setText(_translate("MainWindow", "Add money"))
        self.RTDB_Button.setText(_translate("MainWindow", "Return to dashboard"))
        self.Add_Button.setText(_translate("MainWindow", "Add"))
        self.Money_Line.setPlaceholderText(_translate("MainWindow", "Insert desired amount of money here"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
