import os, json, operator
from datetime import datetime
import data_io


class DK:
    def __init__(self, name, mail, password, age, first_signup, first_login, win_toan, win_doanso, win_xijack, join_xijack):

        self.name = name
        self.age = age
        self.mail = mail
        self.password = password
        self.first_signup = False
        self.first_login = False
        self.win_toan = False
        self.win_doanso = False
        self.win_xijack = False
        self.join_xijack = False



    def update(self, new_data:dict):
        for key, value in new_data.items():
            # chỉ khi nào có thuộc tính thì mới update
            if value:
                setattr(self, key, value)

class accDatabase:
    def __init__(self):
        # Tạo danh sách chứa các player - dạng object
        self.acc_list = list()
        # Đọc dữ liệu khi khởi tạo - dạng dict
        self.acc_dict = data_io.load_json_data()
        self.load_data()  # Gọi phương thức load_data ngay khi khởi tạo

    def load_data(self):
        new_acc = []  # Khởi tạo danh sách trước khi sử dụng
        for acc_data in self.acc_dict:
            acc = DK(name=acc_data['name'],
                     mail=acc_data['mail'],
                     password=acc_data['password'],
                     age=acc_data['age'],
                     first_signup=False,
                     first_login=False,
                     win_doanso=False,
                     win_toan=False,
                     win_xijack=False,
                     join_xijack=False
                     )
            new_acc.append(acc)  # Thêm object DK vào danh sách
        self.acc_list = new_acc  # Gán danh sách mới cho acc_list

    def check_login(self, username, password):
        for acc in self.acc_list:
            if acc.mail == username and acc.password == password:
                return True  # Nếu tìm thấy tài khoản đúng, trả về True
        return False  # Nếu không tìm thấy, trả về False

    def items_to_data(self):
        json_data = list()
        for player in self.players_list:
            json_data.append(player.__dict__)
        return json_data

    def show_all(self):
        for player in self.players_list:
            print(player.__dict__)

    def add_acc(self, acc_dict):
        # Tạo đối tượng từ dữ liệu đầu vào
        # acc_dict['id'] = len(self.acc_list)
    
        new_acc = DK(name=acc_dict['name'],
                     age=acc_dict['age'],
                     mail=acc_dict['mail'],
                     password=acc_dict['password'],
                     first_signup=False,
                     first_login=False,
                     win_doanso=False,
                     win_toan=False,
                     win_xijack=False,
                     join_xijack=False
                     )

        # Thêm vào danh sách object
        self.acc_list.append(new_acc)  # Đổi acc_new thành new_acc

        # Chỉnh sửa danh sách dict
        self.acc_dict.append(acc_dict)

        # Ghi vào file JSON khi thêm tài khoản mới
        data_io.write_json_data(self.acc_dict)

