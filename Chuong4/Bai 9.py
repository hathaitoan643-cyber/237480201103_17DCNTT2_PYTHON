n = int(input("Nhập 1 số nguyên: "))
str_n = str(n)
str_n_format = ""
do_dai = len(str_n)
for i, chu_so in enumerate(str_n):
    str_n_format += chu_so
    if (i + 1) % 3 == 0 and i != do_dai - 1:
        str_n_format += "."

print("Số đã định dạng: " + str_n_format)
