import os, json, operator
from datetime import datetime
import o_data_io

class User:
    def __init__(self, username, password, money, rngnum, slotnum):
        self.username = str(username)
        self.password = str(password)
        self.money = float(money)
        self.rngnum = int(rngnum)
        self.slotnum = int(slotnum)

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
        self.users_dict = o_data_io.load_json_data()
    
    # Chuyển đổi dữ liệu json sang object
    def load_data(self):
        new_users = []
        for user_data in self.users_dict:
            user = User(username = user_data["username"],
                        password = user_data["password"],
                        money = user_data["money"],
                        user = user_data["rngnum"],
                        slotnum = user_data["slotnum"])
            new_users.append(user)
        self.users_list = new_users

    # Chuyển đổi dữ liệu object sang json
    def items_to_data(self):
        json_data = list()
        for user in self.users_list:
            json_data.append(user.__dict__)
        return json_data
    
    # Thêm user mới
    def add_user(self, username, password, money, rngnum, slotnum):
        obj_user = User(username, password, money, rngnum, slotnum)
        dict_user = {
            "username": username,
            "password": password,
            "money": money,
            "rngnum": rngnum,
            "slotnum": slotnum
        }
        # Thêm vào danh sách object
        self.users_list.append(obj_user)
        # Thêm vào danh sách dict
        self.users_dict.append(dict_user)
        # Ghi vào file json
        o_data_io.write_json_data(self.users_dict)

    # Tìm object bằng thuộc tính username
    def find_player_by_name(self, username):
        for user in self.users_dict:
            # Tìm thấy
            if user['username'] == username:
                return True
        # Không tìm thấy
        return False
    
    # Check user login
    def check_login(self, username, password):
        for user in self.users_dict:
            # Tìm thấy
            if user['username'] == username and user['password'] == password:
                return list([True, user])
        # Không tìm thấy
        return list([False, None])
    
    def check_regi(self, username):
        for user in self.users_dict:
            # Tìm thấy
            if user['username'] == username:
                return False
        # Không tìm thấy
        return True
    
    def get_username(self):
        username_list = []
        for user in self.users_list:
            username_list.append(user.username)
        return username_list
    
    def get_user_by_stat(self, stat, rank): # Stat is an interger (0 is money, 1 is rngnum, 2 is slotnum) // Rank is an interger
        stat_sort = []
        if stat != 0 or stat != 1 or stat != 2:
            return False
        if stat == 0:
            stat = "money"
        elif stat == 1:
            stat = "rngnum"
        else:
            stat = "slotnum"
        
        try:
            for user in self.users_dict:
                stat_sort.append(user[stat])
            stat_sort = stat_sort.sort()
            
            for user in self.users_dict:
                if user[stat] == stat_sort[rank*-1]:
                    return user
        except:
            return False

