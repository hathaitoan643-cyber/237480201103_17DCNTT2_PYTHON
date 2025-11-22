n = int(input("Nhập n nguyên dương: "))
if n <= 0:
    print("Yêu cầu nhập n > 0 !")
else:
    print(f"Bảng cửu chương {n} là:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")