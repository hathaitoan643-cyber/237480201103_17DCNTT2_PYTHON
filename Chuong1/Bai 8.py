n = int(input("Nhập n = "))
if (n < 1000) or (n > 9999):
    print("Yêu cầu nhập số nguyên có 4 chữ số !")
else:
    n_str = str(n)
    s = 0
    for i in n_str:
        s += int(i)
    print("Tổng các chữ số vừa nhập:", s)