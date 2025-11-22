L = input("Nhập dãy số nguyên, cách nhau bằng khoảng trắng: ")
number_list = [int(x) for x in L.split()]
if len(number_list) < 3:  # Không tạo được cấp số cộng với 2 số trở xuống
    print("None")
else:
    congsai = number_list[1] - number_list[0]
    is_cap_so_cong = True
    for i in range(2, len(number_list)):
        if number_list[i] != number_list[i - 1] + congsai:
            is_cap_so_cong = False
            break
    if is_cap_so_cong:
        print("Công sai là:", congsai)
    else:
        print("None")
