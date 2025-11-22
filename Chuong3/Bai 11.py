def Inputab():
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    return a, b


# Tìm UCLN của 2 số
def FindUCLN(a, b):
    while b:
        temp = a
        a = b
        b = temp % b
    return a


# kiểm tra 2 số có là nguyên tố cùng nhau
def KTNTCN(a, b):
    t = FindUCLN(a, b)
    if t == 1:
        return True
    else:
        return False


# Tìm BCNN của 2 số
def FindBCNN(a, b):
    t = FindUCLN(a, b)
    if a == 0 or b == 0:
        return 0
    else:
        return abs(a * b) // t


# kiểm tra chương trình
x, y = Inputab()
ucln = FindUCLN(x, y)
bcnn = FindBCNN(x, y)
print(f"Ước chung lớn nhất của {x} và {y} là {ucln}")
print(f"Bội chung nhỏ nhất của {x} và {y} là {bcnn}")
ntcn = KTNTCN(x, y)
if ntcn:
    print(f"{x} và {y} là nguyên tố cùng nhau")
else:
    print(f"{x} và {y} không là nguyên tố cùng nhau")

