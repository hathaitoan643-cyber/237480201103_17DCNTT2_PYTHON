with (open("G:\\BT_py\\CHUONG2\\kinhdoanh.inp.txt", "r", encoding='utf-8') as f_in,
      open("kinhdoanh.out.txt", "w", encoding='utf-8') as f_out):
    n = int(f_in.readline())
    profit = 0
    for _ in range(n):
        m, b = map(int, f_in.readline().split())
        profit += b - m
    f_out.write(str(profit))