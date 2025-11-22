L = input("Nhập dãy số nguyên, cách nhau bằng khoảng trắng: ")
number_list = [int(x) for x in L.split()]
min_list = []
for kt in number_list:
    if kt < 0:
        min_list.append(kt)
if len(min_list) == 0 or all(x >= 0 for x in min_list):
    max_minvalue = 0
else:
    max_minvalue = max(min_list)
print("Giá trị âm lớn nhất trong danh sách là:", max_minvalue)