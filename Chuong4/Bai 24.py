L = input("Nhập dãy số nguyên, cách nhau bằng khoảng trắng: ")
number_list = [int(x) for x in L.split()]
count = 0
max_value = float('-inf')
for kt in number_list:
    if kt > max_value:
        count += 1
        max_value = kt
print("Số lượng giá trị thỏa tính chất: ", count-1)