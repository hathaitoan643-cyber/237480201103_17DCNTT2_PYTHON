n = int(input("Nhập n nguyên dương: "))
if n <= 0:
    print("Yêu cầu nhập n > 0 !")
else:
    if n <= 1:
        kt = False
    else:
        kt = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                kt = False
                break
    if kt:
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không phải là số nguyên tố")