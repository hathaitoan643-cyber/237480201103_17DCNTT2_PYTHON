with (open("G:\\BT_py\\CHUONG2\\chuoi.inp.txt", "r", encoding='utf-8') as f_in,
        open("chuoi.out.txt", "w", encoding='utf-8') as f_out):
    data = f_in.readline().strip()
    letters = ''.join(filter(str.isalpha, data))
    numbers = ''.join(filter(str.isdigit, data))
    if not letters:
        letters = "-"
    if not numbers:
        numbers = "-"
    f_out.write(letters + "\n")
    f_out.write(numbers)
