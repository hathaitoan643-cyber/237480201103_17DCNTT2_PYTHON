t = int(input("Nhập số tiền của bạn: "))
if t % 1000 != 0:
    print("Yêu cầu nhập số tiền chia hết cho 1.000 !")
else:
    Namchuc = int(t / 50000)
    t = t % 50000
    Haichuc = int(t / 20000)
    t = t % 20000
    Muoingan = int(t / 10000)
    t = t % 10000
    Namngan = int(t / 5000)
    t = t % 5000
    Haingan = int(t / 2000)
    t = t % 2000
    Motngan = int(t / 1000)
    t = t % 1000
    print(f"Có {Namchuc} tờ 50.000")
    print(f"Có {Haichuc} tờ 20.000")
    print(f"Có {Muoingan} tờ 10.000")
    print(f"Có {Namngan} tờ 5.000")
    print(f"Có {Haingan} tờ 2.000")
    print(f"Có {Motngan} tờ 1.000")
