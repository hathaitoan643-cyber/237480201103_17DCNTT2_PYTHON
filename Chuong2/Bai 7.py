with (open("G:\\BT_py\\CHUONG2\\2to10.inp.txt", "r", encoding='utf-8') as f_in,
      open("2to10.out.txt", "w", encoding='utf-8') as f_out):
    data = f_in.read().split()
    for bin_n in data:
        dec_n = int(bin_n, 2)
        f_out.write(str(dec_n) + "\n")