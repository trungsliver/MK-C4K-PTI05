import sys
from PyQt6 import QtCore, QtGui, QtWidgets
import ui_login
import ui_regi
import ui_addmoney
import ui_dashboard
import ui_roller
import ui_slotmachine
import o_objects
import o_data_io
from random import randint
import math
import time

# QApplication: Manages the User Interface of the app
# QMainWindow: Creates the main window of the app
# pyside6-rcc img_rc.qrc -o img-rc.py: Converts the image to a python file
# pyuic6 -x zzui_dashboard.ui -o ui_dashboard.py: Converts the UI file to a python file
# pyuic6 -x zzui_solsrng.ui -o ui_roller.py: Converts the UI file to a python file
# pyuic6 -x zzui_slotmachine.ui -o ui_slotmachine.py: Converts the UI file to a python file
# pyuic6 -x zzui_addmoney.ui -o ui_addmoney.py: Converts the UI file to a python file
# pyuic6 -x zzui_gamblers.ui -o ui_users.py: Converts the UI file to a python file

ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
dtb = o_objects.UserDatabase()
account_used = None

rolllist = {
    "Angellic": ["Angellic", 255, 400, "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(182, 182, 0, 255), stop:1 rgba(109, 109, 0, 255))"],
    "Legendary": ["Legendary", 64, 150, "rgb(177, 0, 0)"],
    "Epic": ["Epic", 16, 30, "rgb(77, 0, 177)"],
    "Rare": ["Rare", 8, 15, "rgb(0, 0, 177)"],
    "Unusual": ["Unusual", 4, 5, "rgb(0, 177, 0)"],
    "Common": ["Common", 1, 1, "rgb(0, 0, 0)"],
}

def msg_box(title, content):
    msg = QtWidgets.QMessageBox()
    msg.setStyleSheet("QLabel{min-width: 200px;}"
                          "QLabel{max-width: 200px;}"
                          "QMessageBox{background-color: rgba(233, 233, 233, 255);}"
                          "QPushButton{background-color:rgba(200, 200, 200, 255);"
                          "QLabel{color:rgb(0,0,0);}"
                          "QPushButton{color:rgb(0,0,0);}")
    msg.setWindowTitle(title)
    msg.setInformativeText(content)
    msg.exec()

def UpdateCurrUser():
    jsondata = o_data_io.load_json_data()
    lennum = 0
    for i in jsondata:
        if i["username"] == account_used["username"]:
            jsondata[lennum] = account_used
            break
        lennum += 1
    o_data_io.write_json_data(jsondata)

def RegiUi():
    global ui
    ui = ui_regi.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.Regi_Button.clicked.connect(Regi)
    ui.Switch_Button.clicked.connect(LoginUi)
    MainWindow.show()

def Regi():
    global dtb
    
    name = ui.Name_Line.text().strip()
    passw = ui.Passw_Line.text().strip()
    confirm = ui.Conf_Line.text().strip()
    
    errors = []
    check = True
    
    if name == "" or passw == "" or confirm == "":
        errors.append("Missing values")
        check = False
    
    if len(passw) < 8:
        errors.append("Password is too short")
        check = False
    
    if confirm != passw:
        errors.append("Confirm doesn't mach password")
        check = False
    
    check2 = dtb.check_regi(username=name)
    
    if check2 == False:
        errors.append("Unoriginal name")
        check = False
    
    if check == True:
        dtb.add_user(username=name, password=passw, money=0, rngnum=0, slotnum=0)
        ui.Error_Label.setStyleSheet("color: rgb(0, 177, 0);")
        ui.Error_Label.setText("Registration successful! Now switch to Login to log in.")
    else:
        errortext = ""
        
        for i in errors:
            errortext += f"{i}, "
        
        ui.Error_Label.setStyleSheet("color: rgb(255, 0, 0);")
        ui.Error_Label.setText(f"Error: {errortext}")


def LoginUi():
    global ui
    ui = ui_login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.Login_Button.clicked.connect(Login)
    ui.Switch_Button.clicked.connect(RegiUi)
    ui.Dash_Button.clicked.connect(DashAtt)
    MainWindow.show()

def Login():
    global dtb
    global account_used
    
    name = ui.Name_Line.text().strip()
    passw = ui.Passw_Line.text().strip()
        
    check = dtb.check_login(name, passw)
    print(check)
    
    if True in check:
        account_used = dict(check[1])
        ui.Error_Label.setStyleSheet("color: rgb(0, 177, 0);")
        ui.Error_Label.setText(f"Login succesful! Hello {account_used["username"]}! Now go to the dashboard.")
    else:
        ui.Error_Label.setStyleSheet("color: rgb(255, 0, 0);")
        ui.Error_Label.setText("Error: Incorrect username or password")

def DashAtt():
    j = f"{type(account_used)}"
    print(j)
    print(account_used)
    if j == "<class 'dict'>":
        DashUi()
    else:
        ui.Error_Label.setStyleSheet("color: rgb(255, 0, 0);")
        ui.Error_Label.setText("Error: You ain't have no account used yet")

def DashUi():
    global ui
    ui = ui_dashboard.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.Slot_Button.clicked.connect(SlotUi)
    ui.Money_Button.clicked.connect(AddMoneyUi)
    ui.Roller_Button.clicked.connect(RollerUi)
    ui.Switch_Button.clicked.connect(LoginUi)
    MainWindow.show()

def AddMoneyUi():
    global ui
    ui = ui_addmoney.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.RTDB_Button.clicked.connect(DashUi)
    ui.Add_Button.clicked.connect(AddMoney)
    MainWindow.show()

def AddMoney():
    try:
        money = float(ui.Money_Line.text().strip())
        print("j")
        account_used.update({"money": account_used["money"]+money})

        UpdateCurrUser()
        
        ui.Error_Label.setStyleSheet("color: rgb(0, 177, 0);")
        ui.Error_Label.setText(f"Money added! Current balance: {account_used["money"]}")
    except:
        ui.Error_Label.setStyleSheet("color: rgb(255, 0, 0);")
        ui.Error_Label.setText(f"Error: Either you put nothing in or you put text in.")

def RollerUi():
    global ui
    ui = ui_roller.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.RTDB_Button.clicked.connect(ReturnFromGambling)
    ui.Roll_Button.clicked.connect(Roll)
    MainWindow.show()

def ReturnFromGambling():
    msg_box("Wait!", "Remember, 99 percent of gamblers quit before they win big, so try reentering and roll one more time to win like, idk, 1 morbillion dollars?")
    DashUi()

def Roll():
    global rolllist
    rarities = list(rolllist)
    found = False
    if ui.Price_Rollbox.value() > account_used["money"]:
        ui.Error_Label.setStyleSheet("color: rgb(255, 0, 0);")
        ui.Error_Label.setText(f"Error: Broke alert! Go get some money!")
    else:
        for i in range(len(rarities)):
            if found == False:
                rolled = randint(1, math.ceil(rolllist[rarities[i]][2]/(ui.Price_Rollbox.value()/2)))
                if rolled == 1:
                    ui.Text_Label.setText(str(rarities[i]))
                    ui.Rarity_Label.setText(f"1 in {rolllist[rarities[i]][1]}")
                    ui.Text_Label.setStyleSheet(f"color: {rolllist[rarities[i]][-1]}")
                    ui.Rarity_Label.setStyleSheet(f"color: {rolllist[rarities[i]][-1]}")
                    ui.Earn_Label.setText(f"+{rolllist[rarities[i]][2]}")

                    account_used["money"] += rolllist[rarities[i]][2]
                    account_used["money"] -= ui.Price_Rollbox.value()
                    UpdateCurrUser()
                    found = True


def SlotUi():
    global ui
    ui = ui_slotmachine.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.RTDB_Button.clicked.connect(ReturnFromGambling)
    ui.Roll_Button.clicked.connect(RollSlot)
    MainWindow.show()

def getRolledNumbers():
    return [int(ui.Slot1_Line.text()), int(ui.Slot2_Line.text()), int(ui.Slot3_Line.text())]

def Randomize():
    ui.Slot1_Line.setText(f"{randint(1, 9)}")
    ui.Slot2_Line.setText(f"{randint(1, 9)}")
    ui.Slot3_Line.setText(f"{randint(1, 9)}")

def RollSlot():
    if account_used["money"] < 25:
        ui.Error_Label.setStyleSheet("color: rgb(255, 0, 0);")
        ui.Error_Label.setText(f"Error: Broke alert! Go get some money!")
    else:
        Randomize()
        returnNums = getRolledNumbers()
        # Cases
        if returnNums[2] == returnNums[1]+1 and returnNums[1] == returnNums[0]+1:
            
            if randint(1, 3) == 1: # The "So Close!!1!!11one!!111!" effect
                if int(ui.Slot3_Line.text()) > 1 and int(ui.Slot3_Line.text()) < 9:
                    if randint(1, 2) == 1:
                        ui.Slot3_Line.setText(f"{int(ui.Slot3_Line.text())+1}")
                    else:
                        ui.Slot3_Line.setText(f"{int(ui.Slot3_Line.text())-1}")
                        
                elif int(ui.Slot3_Line.text()) == 1:
                    ui.Slot3_Line.setText(f"{int(ui.Slot3_Line.text())+1}")
                    
                else:
                    ui.Slot3_Line.setText(f"{int(ui.Slot3_Line.text())-1}")
                    
                ui.Earn_Label.setText("+0")
                pass
                
            account_used["money"] += int(f"{returnNums[0]}{returnNums[1]}{returnNums[2]}")*20
            account_used["money"] -= 25
            UpdateCurrUser()
            moneyGot = int(f"{returnNums[0]}{returnNums[1]}{returnNums[2]}")*20
            ui.Earn_Label.setText(f"+{moneyGot}")

        elif returnNums[0] == returnNums[1] and returnNums[1] == returnNums[2]:
            
            if randint(1, 3) == 1: # The "So Close!!1!!11one!!111!" effect
                if int(ui.Slot3_Line.text()) > 1 and int(ui.Slot3_Line.text()) < 9:
                    if randint(1, 2) == 1:
                        ui.Slot3_Line.setText(f"{int(ui.Slot3_Line.text())+1}")
                    else:
                        ui.Slot3_Line.setText(f"{int(ui.Slot3_Line.text())-1}")
                        
                elif int(ui.Slot3_Line.text()) == 1:
                    ui.Slot3_Line.setText(f"{int(ui.Slot3_Line.text())+1}")
                    
                else:
                    ui.Slot3_Line.setText(f"{int(ui.Slot3_Line.text())-1}")
                    
                ui.Earn_Label.setText("+0")
                pass
            
            account_used["money"] += int(f"{returnNums[0]}{returnNums[1]}{returnNums[2]}")*20
            account_used["money"] -= 25
            UpdateCurrUser()
            moneyGot = int(f"{returnNums[0]}{returnNums[1]}{returnNums[2]}")*20
            ui.Earn_Label.setText(f"+{moneyGot}")
        
        else:
            ui.Earn_Label.setText("+0")


RegiUi()
sys.exit(app.exec())