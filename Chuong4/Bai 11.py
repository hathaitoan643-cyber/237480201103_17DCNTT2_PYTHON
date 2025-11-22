L = input("Nhập dãy số nguyên, cách nhau bằng khoảng trắng: ")
number_list = [int(x) for x in L.split()]
max_value = max(number_list)
print("Giá trị lớn nhất trong danh sách là:", max_value)
