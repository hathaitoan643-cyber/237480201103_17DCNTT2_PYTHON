L = input("Nhập dãy số nguyên, cách nhau bằng khoảng trắng: ")
number_list = [int(x) for x in L.split()]
fpos = -1
for kt in number_list:
    if kt > 0:
        fpos = kt
        break
print("Giá trị dương đầu tiên trong danh sách là:", fpos)
