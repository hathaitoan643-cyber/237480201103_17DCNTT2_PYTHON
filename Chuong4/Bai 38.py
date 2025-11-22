# Khởi tạo danh sách sinh viên rỗng
list_sv = {}


# Hàm để thêm sinh viên
def ThemSV():
    ma_sv = input("Nhập MSSV: ")
    ten_sv = input("Nhập tên SV: ")
    list_sv[ma_sv] = ten_sv


# Hàm để xóa sinh viên
def XoaSV():
    ma_sv = input("Nhập mã sinh viên cần xóa: ")
    if ma_sv in list_sv:
        del list_sv[ma_sv]
    else:
        print(f"Không tìm thấy sinh viên có mã {ma_sv}")


# Hàm để sửa thông tin sinh viên
def SuaSV():
    ma_sv = input("Nhập MSSV cần sửa: ")
    if ma_sv in list_sv:
        ten_moi = input("Nhập tên mới cho SV: ")
        list_sv[ma_sv] = ten_moi
    else:
        print(f"Không tìm thấy sinh viên có mã {ma_sv}")


# Hàm để xem danh sách sinh viên
def XemSV():
    print("------------------Danh sách sinh viên-----------------")
    for ma_sv, ten_sv in list_sv.items():
        print(f"MSSV: {ma_sv}, Tên SV: {ten_sv}")
    print("------------------------------------------------------")

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


















