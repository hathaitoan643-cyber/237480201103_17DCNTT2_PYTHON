class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __del__(self):
        print(f"Sinh viên {self.id} đã được xóa.")