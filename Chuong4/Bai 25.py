L = input("Nhập dãy số nguyên, cách nhau bằng khoảng trắng: ")
number_list = [int(x) for x in L.split()]
list_c = []
list_l = []
list_0 = []
for kt in number_list:
    if kt == 0:
        list_0.append(kt)
    else:
        if kt % 2 == 0:
            list_c.append(kt)
        else:
            list_l.append(kt)
list_kq = list_c + list_0 + list_l
print("Danh sách đã sắp xếp như yêu cầu: ",list_kq)
