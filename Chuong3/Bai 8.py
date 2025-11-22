def ktNT(a):
    if a <= 1:
        return False
    else:
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        return True


def FindNT(L, a):
    list_l = []
    for num in L:
        if ktNT(num):
            list_l.append(num)
            if len(list_l) == a:
                break
    return list_l


list_numbers = [2, 4, 6, -11, 13, 7, 13, 2]
t = 6
kq = FindNT(list_numbers, t)
print(kq)