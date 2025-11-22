m = float(input("Nhập m: "))
s = 1
n = 1
while s <= m:
    n += 1
    s += 1 / n
print(f"Với m = {m} thì n = {n} là nhỏ nhất với s = {s} > {m}")