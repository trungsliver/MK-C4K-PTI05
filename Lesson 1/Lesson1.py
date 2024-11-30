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
    # Thêm phần tử vào vị trí chỉ định
user_new2 = Account('minhtu', 'jqk')
users.insert(1, user_new2)
    # Chỉnh sửa phần tử 
users[0].password = '1234'
    # Xóa phần tử theo index
users.pop(1)    # xóa tubeo

# Duyệt danh sách
    # Cách 1: dùng cả index và value
# for i in range(len(users)):
#     print(f"User {i+1}: {users[i].username} - {users[i]. password}")
#     # Cách 2: chỉ dùng value
for user in users:
    print(f"User: {user.username} - {user.password}")
    
# Kiểm tra đăng nhập
input_user = 'tuanminh'
input_pass = '456'
    # Cách 1: không dùng phương thức
check_login1 = False
for user in users:
    if user.username == input_user and user.password == input_pass:
        check_login1 = True
print('Login 1:', check_login1)

    # Cách 2: Dùng Phương thức
check_login2 = False
for user in users:
    if user.login(input_user, input_pass):
        check_login2 = True
print('Login 2:', check_login2)
