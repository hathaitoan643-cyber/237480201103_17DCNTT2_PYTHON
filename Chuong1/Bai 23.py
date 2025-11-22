n = int(input("Nhập n nguyên dương: "))
if n <= 0:
    print("Yêu cầu nhập n > 0 !")
else:
    n_str = len(str(n))
    print(f"{n} có {n_str} chữ số")