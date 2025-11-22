s = input("Nhập chuỗi: ")
c_h = 0
c_t = 0
c_s = 0
c_db = 0
for kt in s:
    if kt.isupper():
        c_h += 1
    elif kt.islower():
        c_t += 1
    elif kt.isdigit():
        c_s += 1
    else:
        c_db += 1

if len(s) >= 6 and c_h >= 1 and c_t >= 1 and c_s >= 1 and c_db >= 1:
    print("Mật khẩu mạnh! ")
else:
    print("Mật khẩu không mạnh! ")
