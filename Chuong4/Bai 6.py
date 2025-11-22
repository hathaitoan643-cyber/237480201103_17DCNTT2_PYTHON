s = input("Nhập chuỗi: ")
t = 0
list_n = []
for kt in s:
    if kt.isdigit():
        t += int(kt)
        list_n.append(int(kt))
print(list_n)
print("Tổng: ", t)
