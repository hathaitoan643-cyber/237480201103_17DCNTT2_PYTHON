import math
with open("bai1.txt", "w", encoding='utf-8') as f:
    n = int(input("Nhập n: "))
    for i in range(1, n + 1):
        sqrt = int(math.sqrt(i))
        if sqrt ** 2 == i:
            f.write(str(i) + " ")