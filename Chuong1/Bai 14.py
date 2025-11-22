a = float(input("Nhập điểm Văn: "))
b = float(input("Nhập điểm Toán: "))
c = float(input("Nhập điểm Tiếng Anh: "))
tb = (a + b + c) / 3
print("Điểm trung bình: ", tb)
if tb >= 8.5:
    if b >= 9 and b > a and b > c:
        print("Đậu chuyên Toán")
    elif a >= 9 and a > c:
        print("Đậu chuyên Văn")
    elif c >= 8.0:
        print("Đậu chuyên Tiếng Anh")
    else:
        print("Đậu chuyên Tin học")
else:
    print("Không đậu chuyên")