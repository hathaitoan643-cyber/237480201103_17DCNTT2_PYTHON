import math
r = float(input("Nhập bán kính hình trụ: "))
h = float(input("Nhập chiều cao hình trụ: "))
Sxq = 2 * math.pi * r * h
Stp = 2 * math.pi * r * (h + r)
V = math.pi * r * r * h
print("Diện tích xung quanh: ", round(Sxq, 2))
print("Diện tích toàn phần: ", round(Stp, 2))
print("Thể tích: ", round(V, 2))