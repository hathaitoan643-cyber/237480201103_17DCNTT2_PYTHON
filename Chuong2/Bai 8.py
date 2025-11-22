with (open("G:\\BT_py\\CHUONG2\\thuaso.inp.txt", "r", encoding='utf-8') as f_in,
        open("thuaso.out.txt", "w", encoding='utf-8') as f_out):
    tsnt = []
    for line in f_in:
        data = int(line.strip())
        i = 2
        elements = []
        while i <= data:
            if data % i == 0:
                elements.append(i)
                data = data // i
            else:
                i += 1
        tsnt.append(elements)
    for elements in tsnt:
        f_out.write(" ".join(map(str, elements)) + "\n")