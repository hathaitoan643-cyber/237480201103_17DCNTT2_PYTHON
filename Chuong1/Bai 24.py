n = int(input("Nhập n nguyên dương: "))
if n <= 0:
    print("Yêu cầu nhập n > 0 !")
else:
    dc = 0
    dl = 0
    n_str = str(n)
    for i in n_str:
        sn = int(i)
        if sn % 2 == 0:
            dc += 1
        else:
            dl += 1
    print(f"Số {n} có {dc} chữ số chẵn và {dl} chữ số lẻ")