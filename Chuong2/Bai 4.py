with (open("G:\\BT_py\\CHUONG2\\INPUT4.txt", "r", encoding='utf-8') as f_in,
      open("OUTPUT4.txt", "w", encoding='utf-8') as f_out):
    n = int(f_in.readline())
    data = f_in.readline().split()
    for i in data:
        num = int(i)
        if num % 2 == 0:
            f_out.write(str(num) + " ")