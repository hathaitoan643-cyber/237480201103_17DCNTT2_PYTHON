with (open("G:\\BT_py\\CHUONG2\\soban.inp.txt", "r", encoding='utf-8') as f_in,
      open("soban.out.txt", "w", encoding='utf-8') as f_out):
    k = int(f_in.readline())
    for m in range(1, k):
        for n in range(m + 1, k + 1):
            sum_m = sum([i for i in range(1, m) if m % i == 0])
            sum_n = sum([i for i in range(1, n) if n % i == 0])
            if sum_m == n and sum_n == m:
                f_out.write(f"{m} {n}\n")