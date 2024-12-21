from oop import Student, StudentList
import os, json

# Tạo 2 objects student
stu1 = Student('Bao Phuc', 15, 10)
stu2 = Student('Duc Tung', 13, 8)

# Khởi tạo danh sách students và thêm phần tử
stu_list = StudentList()
stu_list.add_students(stu1)
stu_list.add_students(stu2)

stu_list.show_students()

# Chuyển danh sách object thành danh sách dictionary
stu_dict_list = []
for stu in stu_list.students:
    stu_convert = stu.to_dict()
    stu_dict_list.append(stu_convert)

# Ghi danh sách vào file json
    # Cách 1:
with open('Lessons/Test3/students.json', 'w') as file:
    json.dump(stu_dict_list, file, indent=4)
    # Cách 2:
stu_list.w_json('Lessons/Test3/students_2.json')

# Đọc dữ liệu từ file
stu_list.r_json('Lessons/Test3/students_2.json')

