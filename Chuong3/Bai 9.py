def FindThMax(L, a):
    global Maxvalue
    if a <= 0 or a > len(L):
        return None
    for _ in range(a):
        Maxvalue = float('-inf')  # Giả sử giá trị lớn nhất ban đầu = - vô cùng
        for num in L:
            if num > Maxvalue:
                Maxvalue = num
        L.remove(Maxvalue)
    return Maxvalue


list_numbers = [-1, 6, -9, 26, 30]
t = 3
kq = FindThMax(list_numbers, t)
print(kq)
