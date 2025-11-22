n = int(input("Nhập số phần tử n: "))
list_n = []
for i in range(1, n + 1):
    e = int(input(f"Nhập phần tử thứ {i}: "))
    list_n.append(e)
with open("bai3.txt", "w", encoding='utf-8') as f:
    for i in list_n:
        if i % 2 == 0:
            f.write(str(i) + " ")
    f.write("\n")
    for i in list_n:
        if i % 2 == 0 or i % 3 == 0:
            f.write(str(i) + " ")
    f.write("\n")
    s = 0
    for i in list_n:
        s += i
    f.write(str(s) + " ")