n = int(input("Nhập n nguyên dương: "))
if n <= 0:
    print("Yêu cầu nhập n > 0 !")
else:
    t = int(n)
    k = 0
    while n > 0:
        if n % 2 != 0:
            break
        n //= 2
        k += 1
    if n == 1:
        print(f"{t} là dạng 2^k với k = {k}.")
    else:
        print(f"{t} không phải là dạng 2^k.")