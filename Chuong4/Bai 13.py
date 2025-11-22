L = input("Nhập dãy số nguyên, cách nhau bằng khoảng trắng: ")
number_list = [int(x) for x in L.split()]
kt = all(x == number_list[0] for x in number_list)
print(kt)