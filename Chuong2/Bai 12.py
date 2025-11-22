with (open("G:\\BT_py\\CHUONG2\\tgcan.inp.txt", "r", encoding='utf-8') as f_in,
      open("tgcan.out.txt", "w", encoding='utf-8') as f_out):
    n = int(f_in.readline())
    points = []
    for _ in range(n):
        x, y = map(int, f_in.readline().split())
        points.append((x, y))
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                a = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
                b = ((points[i][0] - points[k][0]) ** 2 + (points[i][1] - points[k][1]) ** 2) ** 0.5
                c = ((points[j][0] - points[k][0]) ** 2 + (points[j][1] - points[k][1]) ** 2) ** 0.5
                if a == b or a == c or b == c:
                    count += 1
    if count >= 2:
        count -= 1
        f_out.write(str(count))