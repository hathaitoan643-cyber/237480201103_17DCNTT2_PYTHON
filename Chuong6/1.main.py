from student_management import StudentManagement

def main():
    sm = StudentManagement()
    while True:
        print("1. Thêm sinh viên")
        print("2. Xóa sinh viên")
        print("3. Sửa sinh viên")
        print("4. Tìm kiếm sinh viên")
        print("5. Xem danh sách sinh viên")
        print("6. Thoát")
        choice = input("Chọn chức năng: ")
        if choice == '1':
            id = input("Nhập mã sinh viên: ")
            name = input("Nhập tên sinh viên: ")
            sm.add_student(id, name)
        elif choice == '2':
            id = input("Nhập mã sinh viên cần xóa: ")
            sm.delete_student(id)
        elif choice == '3':
            id = input("Nhập mã sinh viên cần sửa: ")
            new_name = input("Nhập tên mới: ")
            sm.edit_student(id, new_name)
        elif choice == '4':
            id = input("Nhập mã sinh viên cần tìm: ")
            student = sm.search_student(id)
            if student:
                print(f"ID: {student.id}, Name: {student.name}")
            else:
                print("Không tìm thấy sinh viên")
        elif choice == '5':
            sm.display_students()
        elif choice == '6':
            break

if __name__ == "__main__":
    main()
