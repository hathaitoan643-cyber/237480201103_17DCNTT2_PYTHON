import math


# kiểm tra số chẵn
def KTSC(n):
    if n % 2 == 0:
        return True
    else:
        return False


# kiểm tra số hoàn hảo
def KTSHH(n):
    if n <= 0:
        return False
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if s == n:
        return True
    else:
        return False


# kiểm tra số nguyên tố
def KTSNT(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


# kiểm tra số chính phương
def KTSCP(n):
    if n <= 0:
        return False
    sqrt = int(math.sqrt(n))
    if sqrt ** 2 == n:
        return True
    else:
        return False


# Tìm UCLN của 2 số
def FindUCLN(a, b):
    while b:
        temp = a
        a = b
        b = temp % b
    return a


# Tìm BCNN của 2 số
def FindBCNN(a, b):
    t = FindUCLN(a, b)
    if a == 0 or b == 0:
        return 0
    else:
        return abs(a * b) // t


# kiểm tra 2 số có là nguyên tố cùng nhau
def KTNTCN(a, b):
    t = FindUCLN(a, b)
    if t == 1:
        return True
    else:
        return False


# kiểm tra chương trình
num = 100
sc = KTSC(num)
shh = KTSHH(num)
snt = KTSNT(num)
scp = KTSCP(num)
print(sc)
print(shh)
print(snt)
print(scp)
# --------------
num1 = 12
num2 = 19
ucln = FindUCLN(num1, num2)
bcnn = FindBCNN(num1, num2)
print(f"Ước chung lớn nhất của {num1} và {num2} là {ucln}")
print(f"Bội chung nhỏ nhất của {num1} và {num2} là {bcnn}")
ntcn = KTNTCN(num1, num2)
if ntcn:
    print(f"{num1} và {num2} là nguyên tố cùng nhau")
else:
    print(f"{num1} và {num2} không là nguyên tố cùng nhau")
