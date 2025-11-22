def armstrong(a):
    kt = len(str(a))
    s = 0
    for i in str(a):
        s += int(i) ** kt
    return s == a


number = 8208
if armstrong(number):
    print(f"{number} là số Armstrong")
else:
    print(f"{number} không phải là số Armstrong")
