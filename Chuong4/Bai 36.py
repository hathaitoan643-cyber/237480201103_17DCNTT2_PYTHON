def InputSV():
    ds = {}
    while True:
        ten = input("Nhập tên sinh viên (để dừng nhập, nhấn Enter): ")
        if not ten:
            break
        diem = float(input(f"Nhập điểm cho {ten}: "))
        ds[ten] = diem
    return ds


def FindSV(ten, ds):
    if ten in ds:
        return f"{ten} có điểm số là {ds[ten]}"
    else:
        return f"Không tìm thấy thông tin cho sinh viên có tên {ten}"


list_sv = InputSV()
nhap_ten_can_tim = input("Nhập tên sinh viên cần tìm kiếm: ")
kq = FindSV(nhap_ten_can_tim, list_sv)
print(kq)
