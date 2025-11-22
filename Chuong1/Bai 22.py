n = int(input("Nhập n nguyên dương: "))
if n <= 0:
    print("Yêu cầu nhập n > 0 !")
else:
    s = 0
    for i in range(1, n + 1):
        s += i
    print("S = ", s)