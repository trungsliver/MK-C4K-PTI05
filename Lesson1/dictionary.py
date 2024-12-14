# Dictionary - CRUD

# Create - Khởi tạo
dict1 = {}
dict2 = {
    # Cặp giá trị key - value
    'name': 'Trần Đức Tùng',
    'age': 13,
    'hobbies': 'pickleball',
    'address': 'Hà Nội',
}

# Read - Duyệt, hiện phần tử
    # Duyệt toàn bộ key - value
for key, value in dict2.items():
    print(f"{key}: {value}")
    # Truy cập bằng key
print('Tên:', dict2['name'])
    # Sử dụng phương thức get()
print('Tuổi:', dict2.get('age'))
        # Không tồn tại key => None / Giá trị mặc định
print('Trường học:', dict2.get('school'))
print('Bạn gái:',dict2.get('girlfriend', '404 not found'))

# Update - chỉnh sửa
    # Add cặp key - value
dict2['children'] = 'Khang Anh'
    # Update giá trị
dict2['hobbies'] = 'badminton'

# Delete - Xóa phần tử
    # del - xóa phần tử theo key
del dict2['children']
    # pop - xóa phần tử và trả về giá trị
dict2.pop('address')

# Kiểm tra key có tồn tại hay không
print('name' in dict2)      # Output: True
print('parents' in dict2)   # Output: False

# Lấy tất cả key bằng phương thức keys()
print(dict2.keys())
# Lấy tất cả value bằng phương thức values()
print(dict2.values())
# Lấy tất cả cặp key - value bằng phương thức items()
print(dict2.items())

# Hàm map(function, itertable)
    # function: hàm biến đổi phần tử
    # itertable: đối tượng dữ liệu (list, set, ...)

# Ví dụ: Cho 1 danh sách điểm hệ số 10
# Yêu cầu: Dùng map() để chuyển đổi danh sách thành hệ số 4
gpa_10 = [5, 7, 8, 10, 9]
    # Cách 1: lambda - hàm không xác định
gpa_4 = map(lambda gpa: gpa/10 * 4, gpa_10)
# gpa_44 = []
# for gpa in gpa_10:
#     new_gpa = gpa/10 * 4
#     gpa_44.append(new_gpa)
print(list(gpa_4))
    # Cách 2: Dùng hàm xác định
def convert_gpa(score):
    return score / 10 * 4
gpa_4 = map(convert_gpa, gpa_10)
print(list(gpa_4))