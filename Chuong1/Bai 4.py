import math
a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c "))
cv = a + b + c
p = (a + b + c) / 2
dt = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f"Chu vi: {cv} ; Diện tích: {round(dt, 2)}")