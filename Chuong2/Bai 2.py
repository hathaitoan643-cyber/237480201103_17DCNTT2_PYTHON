with open("bai2.txt", "w", encoding='utf-8') as f:
    n = int(input("Nhập n: "))
    for i in range(1, n + 1):
        s = 0
        for j in range(1, i):
            if i % j == 0:
                s += j
        if s == i:
            f.write(str(i) + " ")