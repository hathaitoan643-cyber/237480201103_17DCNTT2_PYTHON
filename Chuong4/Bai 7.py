import re

s = input("Nhập vào một chuỗi: ")
# Sử dụng biểu thức chính quy để tìm tất cả các con số trong chuỗi
so = re.findall(r'\d+', s)
tong = 0
list_n = []
for s in so:
    tong += int(s)
    list_n.append(int(s))

print(list_n)
print("Tổng của các số trong chuỗi là:", tong)