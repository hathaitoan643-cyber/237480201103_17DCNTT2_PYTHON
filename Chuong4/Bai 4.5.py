s = input("Nhập chuỗi: ")
c_h = 0
c_t = 0
c_s = 0
for kt in s:
    if kt.isupper():
        c_h += 1
    elif kt.islower():
        c_t += 1
    elif kt.isdigit():
        c_s += 1

print("Số ký tự hoa: ", c_h)
print("Số ký tự thường: ", c_t)
print("Số ký tự số: ", c_s)
