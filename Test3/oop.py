import json

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # Phương thức hiện đối tượng
    def __str__(self):
        return f"Tên: {self.name}, Tuổi: {self.age}, Lớp: {self.grade}"
    
    def show_info(self):
        print(f"{self.name} - {self.age} - {self.grade}")

    # Phương thức chuyển đổi object thành dicionary
    def to_dict(self):
        return {'name': self.name, 'age': self.age, 'grade': self.grade}
    
    def to_dict2(self):
        return self.__dict__
        
    
# Lớp quản lý
class StudentList:
    def __init__(self):
        self.students = []
    
    # Phương thức thêm học sinh vào danh sách
    def add_students(self, student):
        self.students.append(student)

    # Phương thức hiện toàn bộ danh sách
    def show_students(self):
        for student in self.students:
            print(student.to_dict())

    # Phương thức viết toàn bộ danh sách vào file
    def w_json(self, path):
        # Chuyển đổi danh sách object thành danh sách dictionary
        data = [student.to_dict2() for student in self.students]
        # Viết dữ liệu vào file
        with open(str(path), 'w') as file:
            json.dump(data, file, indent=4)

    # Phương thức đọc dữ liệu từ file
    def r_json(self, path):
        # Đọc dữ liệu từ file
        with open(str(path), 'r') as file:
            data = json.load(file)
        # Chuyển dictionary thành đối tượng
        stu_list = []
        for item in data:
            student = Student(item['name'], item['age'], item['grade'])
            stu_list.append(student)
        # Hiển thị dữ liệu
        for stu in stu_list:
            print(stu)
            # stu.show_info()
