n = int(input("Nhập số nguyên dương n: "))
if n > 0:
    if n % 5 == 0 and n % 7 == 0:
        print(f"{n} là số vừa chia hết cho 5 và chia hết cho 7")
    else:
        print(f"{n} không chia hết cho 5 và 7")
else:
    print("Yêu cầu nhập n > 0 !")