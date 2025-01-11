import sys, os
from PyQt6 import QtGui, QtWidgets, QtCore
import lesson7_p1, oop

# QApplication: quản lý phần giao diện ứng dụng
# QMainWindow: tạo cửa sổ ứng dụng chính

#xu ly
ui = ''
app = QtWidgets.QApplication(sys.argv) 
MainWindow = QtWidgets.QMainWindow()
dsPTI05 = ['Tuan Minh', 'Chi Bao', 'Khang Anh', 'Duc Tung']
dtb = oop.UserDatabase()
dtb.load_data()
def homeUi():
    global ui
    ui = lesson7_p1.Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Thêm danh sách để hiển thị trên list widget
    users = dtb.get_username()
    print(users)
    ui.listWidget.addItems(users)
    # Khai báo sự kiện ấn các nút
    # ui.btn_add.clicked.connect(add_item)
    # ui.btn_edit.clicked.connect(edit_item)
    # ui.btn_delete.clicked.connect(delete_item)
    # ui.btn_search.clicked.connect(search_item)

    MainWindow.show()

def add_item():
    # Lấy text ở lineEdit
    text = ui.lineEdit.text()
    # Thêm phần tử vào danh sách
    dsPTI05.append(str(text))
    # Xóa hết các phần tử trên widget
    ui.listWidget.clear()
    # Thêm lại danh sách
    ui.listWidget.addItems(dsPTI05)
    # Xóa dữ liệu ở lineEdit
    ui.lineEdit.setText('')

def edit_item():
    # Lấy index dòng đang chọn trên list widget
    cur = ui.listWidget.currentRow()
    # Lấy text ở lineEdit
    text = ui.lineEdit.text()
    # Thay thế phần tử tại index
    if cur >= 0:
        dsPTI05[cur] = str(text)
    else:
        msg_box('Lỗi', 'Chưa chọn đối tượng để sửa!')
    # Xóa hết các phần tử trên widget
    ui.listWidget.clear()
    # Thêm lại danh sách
    ui.listWidget.addItems(dsPTI05)
    # Xóa dữ liệu ở lineEdit
    ui.lineEdit.setText('')

def delete_item():
    # Lấy index dòng đang chọn trên list widget
    cur = ui.listWidget.currentRow()
    # Lấy text ở lineEdit
    text = ui.lineEdit.text()
    # Kiểm tra index và xóa
    if 0 <= cur <= len(dsPTI05):
        dsPTI05.pop(cur)
        msg_box('Thành công','Đã xóa đối tượng khỏi danh sách')
    else:
        msg_box('Lỗi', 'Chưa chọn đối tượng để xóa!')
    # Xóa hết các phần tử trên widget
    ui.listWidget.clear()
    # Thêm lại danh sách
    ui.listWidget.addItems(dsPTI05)
    # Xóa dữ liệu ở lineEdit
    ui.lineEdit.setText('')


def search_item():
    cur = ui.listWidget.currentRow()
    insert_txt = ui.lineEdit.text()
    check = False
    check_list = []
    for item in dsPTI05:
        if insert_txt in item:
            check = True
            check_list.append(item)
    
    # Xóa hết các phần tử ở trên widget
    ui.listWidget.clear()
    # add lại cả danh sách vào list widget
    if check == True:
        msg_box('Thành công', f'Có {len(check_list)} kết quả!')
    else:
        check_list.append('item not found')
    ui.listWidget.addItems(check_list)

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

#Run app
homeUi()
sys.exit(app.exec())


# Lưu ý: chuột phải vào folder chứa 2 file này, chọn Open .... terminal
# Câu lệnh convert ui: pyuic6 -x login.ui -o login.py
# Câu lệnh convert ui: pyuic6 -x signup.ui -o signup.py
# Câu lệnh convert qrc: pyside6-rcc img.qrc -o img_rc.py
#  pyuic6 -x lesson7_p1.ui -o lesson7_p1.py