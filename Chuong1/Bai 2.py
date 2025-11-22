s = int(input("Nhập số giây: "))
h = int(s / 3600)
m = (s - (h * 3600)) // 60
g = s - (h * 3600) - (m * 60)
print(f"{h} : {m} : {g}")