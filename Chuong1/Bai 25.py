n = int(input("Nhập n nguyên dương: "))
if n <= 0:
    print("Yêu cầu nhập n > 0 !")
else:
    s = 0
    k = 0
    while s < n:
        k += 1
        s += k
    k -= 1
    s -= k + 1
    print(f"n = {n} => k = {k} và S({k}) = {s} < {n}")