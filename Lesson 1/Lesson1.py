from oop1 import Account

# Khởi tạo danh sách users
users = [
    Account('chibao', '123'),
    Account('tuanminh', '456'),
]

# Chỉnh sửa danh sách
    # Thêm phần tử vào cuối danh sách
user_new = Account('baophuc', '789')
users.append(user_new)
    # Chỉnh sửa phần tử 
users[0].password = '1234'

# Duyệt danh sách
    # Cách 1: dùng cả index và value
for i in range(len(users)):
    print(f"User {i+1}: {users[i].username} - {users[i]. password}")
    # Cách 2: chỉ dùng value
for user in users:
    print(f"User: {user.username} - {user.password}")