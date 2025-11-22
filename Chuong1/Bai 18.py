n = int(input("Nhập n nguyên dương: "))
if n <= 0:
    print("Yêu cầu nhập n > 0 !")
else:
    print(f"Ước của {n} là: ")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)