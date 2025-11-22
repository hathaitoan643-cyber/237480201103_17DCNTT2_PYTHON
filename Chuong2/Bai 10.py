with (open("G:\\BT_py\\CHUONG2\\dayso.inp.txt", "r", encoding='utf-8') as f_in,
      open("dayso.out.txt", "w", encoding='utf-8') as f_out):
    a = [1, 1, 1]
    for line in f_in:
        k = int(line.strip())
        if k <= 3:
            result = 1
        else:
            for i in range(3, k):
                next_num = a[i - 1] + a[i - 3]
                a.append(next_num)
            result = a[-1]
        f_out.write(str(result) + "\n")