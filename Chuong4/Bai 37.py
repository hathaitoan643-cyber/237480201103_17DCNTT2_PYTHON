import array as arr


def InputArr():
    gia_tri = input("Nhập các số nguyên cách nhau bằng dấu phẩy: ").split(',')
    mang = arr.array('i', [int(x) for x in gia_tri])
    return mang


def SapXepTang(mang):
    arrTang = sorted(mang)
    return arrTang


def SapXepGiam(mang):
    t = SapXepTang(mang)
    arrGiam = arr.array('i', list(reversed(t)))
    return arrGiam


a = InputArr()
sxtang = SapXepTang(a)
sxgiam = SapXepGiam(a)
print("Mảng tăng dần:", sxtang)
print("Mảng giảm dần:", sxgiam)
