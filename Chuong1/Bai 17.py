n = int(input("Nhập n nguyên dương: "))
if n <= 0:
    print("Yêu cầu nhập n > 0 !")
else:
    Sc = 0
    Sl = 0
    for i in range(n):
        if i % 2 != 0:
            Sl += i
        else:
            Sc += i
    print(f"Tổng các số lẻ nhỏ hơn {n} là: ", Sl)
    print(f"Tổng các số chẵn nhỏ hơn {n} là: ", Sc)