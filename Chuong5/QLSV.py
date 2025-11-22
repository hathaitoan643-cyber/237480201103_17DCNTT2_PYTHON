# Khởi tạo danh sách sinh viên rỗng
list_sv = []


# Hàm để thêm danh sách sinh viên
def ThemSV():
    ma_sv = input("Nhập MSSV: ")
    found = False
    for sinh_vien in list_sv:
        if sinh_vien[0] == ma_sv:
            print("Mã sinh viên đã tồn tại. Vui lòng nhập mã khác !")
            found = True
            break
    if not found:
        ten_sv = input("Nhập tên SV: ")
        sinh_vien = (ma_sv, ten_sv)
        list_sv.append(sinh_vien)


# Hàm để xóa sinh viên
def XoaSV():
    ma_sv = input("Nhập mã sinh viên cần xóa: ")
    found = False
    for sinh_vien in list_sv:
        if sinh_vien[0] == ma_sv:
            list_sv.remove(sinh_vien)
            found = True
            break

    if not found:
        print(f"Không tìm thấy sinh viên có mã {ma_sv}")


# Hàm để sửa thông tin sinh viên
def SuaSV():
    ma_sv = input("Nhập MSSV cần sửa: ")
    found = False
    for i, sinh_vien in enumerate(list_sv):
        if sinh_vien[0] == ma_sv:
            ten_moi = input("Nhập tên mới cho SV: ")
            list_sv[i] = (ma_sv, ten_moi)
            found = True
            break

    if not found:
        print(f"Không tìm thấy sinh viên có mã {ma_sv}")


# Hàm để xem danh sách sinh viên
def XemSV():
    print("------------------Danh sách sinh viên-----------------")
    for ma_sv, ten_sv in list_sv:
        print(f"MSSV: {ma_sv}, Tên SV: {ten_sv}")
    print("------------------------------------------------------")