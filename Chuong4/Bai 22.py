L = input("Nhập dãy số nguyên, cách nhau bằng khoảng trắng: ")
number_list = [int(x) for x in L.split()]
kt = True
for i in range(len(number_list)):
    for j in range(i + 1, len(number_list)):
        if (number_list[i] + number_list[j]) % 2 == 0:
            kt = False
if kt:
    print("Danh sách này là danh sách chẵn lẻ.")
else:
    print("Danh sách này không phải là danh sách chẵn lẻ.")
