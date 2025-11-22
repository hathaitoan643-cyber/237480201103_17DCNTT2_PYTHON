with open("G:\\BT_py\\CHUONG2\\bieudienso.inp.txt", "r", encoding='utf-8') as f_in, \
        open("bieudienso.out.txt", "w", encoding='utf-8') as f_out:
    n = int(f_in.readline().strip())
    ways = []
    found = False
    for i in range(1, n + 1):
        s = i
        ns = [str(i)]
        for j in range(i + 1, n):
            s += j
            ns.append(str(j))
            if s == n:
                ways.append(ns.copy())
                found = True
                break
            elif s > n:
                break
    if found:
        f_out.write(str(len(ways)) + '\n')
        for way in ways:
            f_out.write(' + '.join(way) + '\n')
    else:
        f_out.write("0 có cách biểu diễn số " + str(n) + '\n')



