# DICTIONARY & MAP
# Bài 1: Cho 1 danh sách gồm tên của học sinh (viết hoa lộn xộn)
# Yêu cầu: Dùng map() để chuyển đổi danh sách trên viết hoa tất cả chữ
# Ví dụ: tRunG -> TRUNG
pti05 = ['tUaN mInH', 'cHi bAo', 'MiNh tU', 'dUC tUNg', 'kHaNG AnH']
    # Cách 1:
pti05_1 = map(lambda stu: str.upper(stu), pti05)
print(list(pti05_1))
    # Cách 2:
def convert_to_upper(item):
    return str.upper(item)
pti05_2 = map(convert_to_upper, pti05)
print(list(pti05_2))

# Bài 2: Quản lý thông tin sinh viên
# #Yêu cầu: Tạo một dictionary lưu trữ thông tin sinh viên với các khóa: name, age, và grade. 
# Thực hiện các thao tác sau:
# 1. Thêm sinh viên với thông tin name = "John", age = 22, và grade = "A".
student = {
    'name': 'John',
    'age': 22,
    'grade': 'A',
}
# 2. Cập nhật grade của sinh viên thành "A+".
student['grade'] = 'A+'
# 3. Xóa thông tin age của sinh viên.
del student['age']
# 4. Kiểm tra xem name có trong dictionary không.
print('name' in student)

# Bài 3: Đếm Số Lần Xuất Hiện Của Từ Trong Chuỗi
# Yêu cầu: Viết chương trình nhận vào một chuỗi và trả về một dictionary đếm số lần xuất hiện của mỗi từ trong chuỗi.
sentence = 'this is a test this is only a test'
def word_count(sentence):
    words = sentence.strip().split()
    # mỗi từ là 1 key, số lần xuất hiện là value
    count_dict = {}
    for word in words:
        count_dict[word] = count_dict.get(word, 0) + 1
    return count_dict
print(word_count(sentence))

# Bài 4: Gộp Hai Dictionary
# Yêu cầu: Cho hai dictionary A và B. Viết chương trình gộp chúng lại. Nếu một key xuất hiện ở cả hai dictionary, cộng giá trị của chúng lại.
A = {'a': 100, 'b': 200, 'c': 300}
B = {'b': 250, 'c': 150, 'd': 400}
def merge_dicts(dict1, dict2):
    # copy dict1 để đảm bảo dữ liệu không bị thay đổi
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        # Nếu key đã tồn tại trong dict1, cộng giá trị
        # Nếu key chưa tồn tại, để giá trị mặc định = value(dict2)
        merged_dict[key] = merged_dict.get(key, 0) + value
    return merged_dict
merged = merge_dicts(A, B)
print(merged)

# Bài 5: Tìm Key Có Giá Trị Lớn Nhất
# Yêu cầu: Cho một dictionary có các cặp {key: value}. Viết chương trình để tìm key có giá trị lớn nhất.
grade = {
    'Tuấn Minh': 1,
    'Chí Bảo': -1.5,
    'Minh Tú': 10,
    'Đức Tùng': 7,
    'Khang Anh': 11
}
def find_max(dict):
    max_key = max(dict, key=dict.get)
    return max_key
print(find_max(grade))

# Bài 6: Sắp Xếp Dictionary Theo Giá Trị
# Yêu cầu: Viết chương trình để sắp xếp một dictionary theo giá trị từ cao đến thấp.
grade = {
    'Tuấn Minh': 1,
    'Chí Bảo': -1.5,
    'Minh Tú': 10,
    'Đức Tùng': 7,
    'Khang Anh': 11
}
def sort_dict_by_value(my_dict):
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict
print(sort_dict_by_value(grade))

# Bài 7: Nhóm Các Phần Tử Theo Giá Trị
# Yêu cầu: Viết chương trình để nhóm các phần tử của một dictionary dựa trên giá trị của chúng. Ví dụ, các phần tử có cùng giá trị sẽ được đưa vào một danh sách.
data = {
    'apple': 1,
    'banana': 2,
    'cherry': 2,
    'bomb': 3,
    'elderberry': 3
}
def group_by_value(my_dict):
    grouped_dict = {}
    for key, value in my_dict.items():
        if value not in grouped_dict:
            grouped_dict[value] = []
        grouped_dict[value].append(key)
    return grouped_dict
print('\n',group_by_value(data))

# Bài 8: Tạo Dictionary Từ Danh Sách
# Yêu cầu: Viết chương trình tạo một dictionary từ hai danh sách: một danh sách chứa key và một danh sách chứa value tương ứng.
keys = ['apple', 'banana', 'cherry']
values = [1, 2, 3]
def list_to_dict(keys, values):
    # zip(): tạo ra các cặp key-value từ 2 danh sách
    # dict(): chuyển các cặp key-value thành dictionary
    return dict(zip(keys, values))
print(list_to_dict(keys, values))
