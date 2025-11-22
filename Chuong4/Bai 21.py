L = input("Nhập dãy số nguyên, cách nhau bằng khoảng trắng: ")
number_list = [int(x) for x in L.split()]
vt = False
for i in range(1, len(number_list) - 1):
    if number_list[i] == number_list[i - 1] * number_list[i + 1]:
        print("Vị trí thỏa mãn:", i)
        vt = True

if not vt:
    print("-1")