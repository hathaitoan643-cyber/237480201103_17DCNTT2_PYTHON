with (open("G:\\BT_py\\CHUONG2\\INPUT6.txt", "r", encoding='utf-8') as f_in,
      open("OUTPUT6.txt", "w", encoding='utf-8') as f_out):
    n = int(f_in.readline())
    data = f_in.readline().split()

    for i in range(len(data)):
        (data[i]) = int(data[i])

    a = data[0]
    b = data[1]

    if a ==0 or b == 0:
        f_out.write(f"UCLN({data[0], data[1]} = {a+b} \n")
        f_out.write(f"BCNN({data[0], data[1]} = 0")
    else:
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        ucln = a
        bcnn = abs(int(data[0]) * int(data[1])) // ucln
        f_out.write(f"UCLN({data[0], data[1]} = {ucln} \n")
        f_out.write(f"BCNN({data[0], data[1]} = {bcnn}")