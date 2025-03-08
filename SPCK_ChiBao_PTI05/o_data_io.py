import os, json

# Đọc dữ liệu (READ)
def load_json_data():
    user_dict_data = list()
    with open('data.json', 'r') as file:
        data = json.load(file)
    user_dict_data.extend(data)
    return user_dict_data

# Ghi dữ liệu (WRITE)
def write_json_data(json_data):
    with open('data.json', 'w') as file:
        json.dump(json_data, file)

# Xem đường dẫn hiện tại
print(os.getcwd()) 