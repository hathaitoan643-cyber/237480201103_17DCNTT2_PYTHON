from giao_vien import GiaoVien
from hoc_sinh import HocSinh

def main():
    gv = None
    hs = None
    while True:
        #Test kế thừa lớp Person
        print("1. Thêm giáo viên")
        print("2. Thêm học sinh")
        print("3. Thoát")
        choice = input("Chọn chức năng: ")
        if choice == '1':
            ho_ten = input("Nhập họ tên: ")
            gioi_tinh = input("Nhập giới tính: ")
            nam_sinh = input("Nhập năm sinh: ")
            noi_sinh = input("Nhập nơi sinh: ")
            dia_chi = input("Nhập địa chỉ: ")
            tham_nien = int(input("Nhập số năm giảng dạy: "))
            hoc_vi = input("Nhập học vị: ")
            gv = GiaoVien(ho_ten, gioi_tinh, nam_sinh, noi_sinh, dia_chi, tham_nien, hoc_vi)
            print(f"Đã thêm giáo viên {gv.ho_ten}")
        elif choice == '2':
            ho_ten = input("Nhập họ tên: ")
            gioi_tinh = input("Nhập giới tính: ")
            nam_sinh = input("Nhập năm sinh: ")
            noi_sinh = input("Nhập nơi sinh: ")
            dia_chi = input("Nhập địa chỉ: ")
            diem_toan = float(input("Nhập điểm Toán: "))
            diem_ly = float(input("Nhập điểm Lý: "))
            diem_hoa = float(input("Nhập điểm Hóa: "))
            hs = HocSinh(ho_ten, gioi_tinh, nam_sinh, noi_sinh, dia_chi, diem_toan, diem_ly, diem_hoa)
            print(f"Đã thêm học sinh {hs.ho_ten}")
        elif choice == '3':
            break

if __name__ == "__main__":
    main()

