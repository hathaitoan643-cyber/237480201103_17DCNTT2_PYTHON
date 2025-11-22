from QLSV import *


def ChucNang():
    while True:
        print("\nChọn chức năng:")
        print("1. Thêm sinh viên")
        print("2. Xóa sinh viên")
        print("3. Sửa sinh viên")
        print("4. Xem danh sách sinh viên")
        print("5. Thoát")

        lua_chon = input("Nhập lựa chọn (1/2/3/4/5): ")
        if lua_chon == "1":
            ThemSV()
        elif lua_chon == "2":
            XoaSV()
        elif lua_chon == "3":
            SuaSV()
        elif lua_chon == "4":
            XemSV()
        elif lua_chon == "5":
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")


ChucNang()

