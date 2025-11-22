L = input("Nhập dãy số nguyên, cách nhau bằng khoảng trắng: ")
number_list = [int(x) for x in L.split()]
sx = sorted(number_list)
print("Danh sách sắp xếp từ bé đến lớn: ",sx)
