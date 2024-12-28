import os, json, operator
from datetime import datetime
import data_io

class Player:
    def __init__(self, id, name, dob, region, club, rating=None, worth=None):
        self.id = id
        self.name = name
        self.dob = dob
        self.region = region
        self.club = club
        # Nếu có thì định dạng float, không thì mặc định = 0
        self.rating = float(rating) if rating else 0
        self.worth = float(worth) if worth else 0

    def update(self, new_data:dict):
        for key, value in new_data.items():
            # chỉ khi nào có thuộc tính thì mới update
            if value:
                setattr(self, key, value)

    def show_info(self):
        print(f"ID: {self.id} \nName: {self.name}")


class PlayerDatabase:
    def __init__(self):
        # Tạo danh sách chứa các player - dạng object
        self.players_list = list()
        # Đọc dữ liệu khi khởi tạo - dạng dict
        self.players_dict = data_io.load_json_data()

    # Chuyển đổi dữ liệu json sang object
    def load_data(self):
        new_players = []
        for player_data in self.players_dict:
            player = Player(id = player_data["id"],
                            name = player_data['name'],
                            dob = player_data['dob'],
                            region = player_data['region'],
                            club = player_data['club'],
                            rating = player_data['rating'],
                            worth = player_data['worth'])
            new_players.append(player)
        self.players_list = new_players

    # Chuyển đổi dữ liệu object sang json
    def items_to_data(self):
        json_data = list()
        for player in self.players_list:
            json_data.append(player.__dict__)
        return json_data
    
    # Tìm object bằng thuộc tính name
    def find_player_by_name(self, name):
        for player in self.players_list:
            # Tìm thấy
            if player.name == name:
                return player
        # Không tìm thấy
        return False
    
    # Thêm 1 player mới
    def add_player(self, player_dict):
        # Tạo đối tượng
            # id sẽ là số index tiếp theo
        player_dict['id'] = len(self.players_list)
        new_player = Player(id = player_dict["id"],
                            name = player_dict['name'],
                            dob = player_dict['dob'],
                            region = player_dict['region'],
                            club = player_dict['club'],
                            rating = player_dict['rating'],
                            worth = player_dict['worth'])
        # Thêm vào danh sách object
        self.players_list.append(new_player)
        # Chỉnh sửa danh sách dict
        self.players_dict.append(player_dict)
        # Ghi vào file json khi thêm đối tượng mới
        data_io.write_json_data(self.players_dict)

    # Tìm tên player và sửa thông tin
    def edit_player(self, edit_name, new_dict):
        # Tìm đối tượng
        matched = self.find_player_by_name(edit_name)
        # Sửa dối tượng
        if matched:
            matched.update(new_dict)
            # viết lại file json khi chỉnh sửa đối tượng
            self.players_dict = self.items_to_data()
            data_io.write_json_data(self.players_dict)

    # Tìm tên player và xóa thông tin
    def delete_player(self, delete_name):
        # Tìm đối tượng
        matched = self.find_player_by_name(delete_name)
        # Xóa đối tượng
        if matched:
            self.players_list.remove(matched)
            # viết lại file json khi chỉnh sửa đối tượng
            self.players_dict = self.items_to_data()
            data_io.write_json_data(self.players_dict)

    # Tìm tên tất cả player có tên là search_name
    def search_player(self, search_name) -> list[Player]:
        matched_items = []
        for player in self.players_list:
            if search_name.lower() in player.name.lower():
                matched_items.append(player)
        return matched_items
    
    # Phương thức sắp xếp theo rating
    def sort_item_by_rating(self, top=None):
        self.players_list = sorted(self.players_list, 
                                      key=operator.attrgetter('rating'),
                                      reverse=True
                                      )
        if top:
            return self.players_list[top]
        
    # Phương thức sắp xếp theo name    
    def sort_item_by_title(self, top=None):
        self.players_list = sorted(self.players_list, 
                                      key=operator.attrgetter('name')
                                      )
        if top:
            return self.players_list[top]
        
    def show_all(self):
        for player in self.players_list:
            print(player.__dict__)