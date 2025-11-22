from student import Student

class StudentManagement:
    def __init__(self):
        self.students = []

    def __del__(self):
        for student in self.students:
            del student
        print("Tất cả sinh viên đã được xóa.")

    def add_student(self, id, name):
        self.students.append(Student(id, name))

    def delete_student(self, id):
        self.students = [student for student in self.students if student.id != id]

    def edit_student(self, id, new_name):
        for student in self.students:
            if student.id == id:
                student.name = new_name

    def search_student(self, id):
        for student in self.students:
            if student.id == id:
                return student
        return None

    def display_students(self):
        for student in self.students:
            print(f"ID: {student.id}, Name: {student.name}")
