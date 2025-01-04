import os, json, operator
from datetime import datetime
import data_io

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def update(self, new_data:dict):
        for key, value in new_data.items():
            # chỉ khi nào có thuộc tính thì mới update
            if value:
                setattr(self, key, value)

    def show_info(self):
        print(f"User: {self.username} \nPass: {self.password}")

class UserDatabase:
    def __init__(self):
        # Tạo danh sách chứa các player - dạng object
        self.users_list = list()
        # Đọc dữ liệu khi khởi tạo - dạng dict
        self.users_dict = data_io.load_json_data()
    
    # Chuyển đổi dữ liệu json sang object
    def load_data(self):
        new_users = []
        for user_data in self.users_dict:
            user = User(username = user_data["username"],
                        password = user_data["password"])
            new_users.append(user)
        self.users_list = new_users

    # Chuyển đổi dữ liệu object sang json
    def items_to_data(self):
        json_data = list()
        for user in self.users_list:
            json_data.append(user.__dict__)
        return json_data
    
    # Thêm user mới
    def add_user(self, username, password):
        obj_user = User(username, password)
        dict_user = {
            "username": username,
            "password": password
        }
        # Thêm vào danh sách object
        self.users_list.append(obj_user)
        # Thêm vào danh sách dict
        self.users_dict.append(dict_user)
        # Ghi vào file json
        data_io.write_json_data(self.users_dict)

    # Tìm object bằng thuộc tính username
    def find_player_by_name(self, username):
        for user in self.users_list:
            # Tìm thấy
            if user.username == username:
                return True
        # Không tìm thấy
        return False
    
    # Check user login
    def check_login(self, username, password):
        for user in self.users_list:
            # Tìm thấy
            if user.username == username and user.password == password:
                return True
        # Không tìm thấy
        return False