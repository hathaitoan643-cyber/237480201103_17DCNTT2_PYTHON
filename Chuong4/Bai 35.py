import array as arr


def InputArr():
    gia_tri = input("Nhập các số nguyên cách nhau bằng dấu phẩy: ").split(',')
    mang = arr.array('i', [int(x) for x in gia_tri])
    return mang


def SoChan(mang):
    so_chan = []
    for so in mang:
        if so % 2 == 0:
            so_chan.append(so)
    return so_chan


a = InputArr()
sc = SoChan(a)
print("Các số chẵn trong mảng:", sc)