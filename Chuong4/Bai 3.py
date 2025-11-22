def sum_sn(chuoi):
    n = chuoi.split(',')
    if len(n) == 3:
        try:
            so1 = int(n[0])
            so2 = int(n[1])
            so3 = int(n[2])
            tong = so1 + so2 + so3
            return tong
        except ValueError:
            return "Chuỗi không chứa ba số nguyên hợp lệ"
    else:
        return "Chuỗi không chứa ba số nguyên"


s = input("Nhập chuỗi có dạng 3 số nguyên: ")
print("Tổng:", sum_sn(s))
