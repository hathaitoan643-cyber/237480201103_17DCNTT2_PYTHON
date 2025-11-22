str_a = input("Nhập chuỗi a: ")
str_b = input("Nhập chuỗi b: ")
kq = ""
i = 0
while i < len(str_a):
    if str_a[i:i+len(str_b)] == str_b:
        i += len(str_b)
    else:
        kq += str_a[i]
        i += 1

print("Sau khi xóa, chuỗi a:", kq)
