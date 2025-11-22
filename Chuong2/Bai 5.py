with (open("G:\\BT_py\\CHUONG2\\INPUT5.txt", "r", encoding='utf-8') as f_in,
      open("OUTPUT5.txt", "w", encoding='utf-8') as f_out):
    n = int(f_in.readline())
    data = f_in.readline().split()

    for i in range(len(data)):
        (data[i]) = int(data[i])

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
    f_out.write(str(data) + " ")