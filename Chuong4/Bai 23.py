L = input("Nhập dãy số nguyên, cách nhau bằng khoảng trắng: ")
number_list = [int(x) for x in L.split()]
kt = False
for i in range(1, len(number_list) - 1):
    if (number_list[i] > number_list[i - 1] and number_list[i] > number_list[i + 1]) or (number_list[i] < number_list[i - 1] and number_list[i] < number_list[i + 1]):
        kt = True
        break

if kt:
    print("True")
else:
    print("False")
