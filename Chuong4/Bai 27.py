L = input("Nhập các phần tử danh sách, cách nhau bằng khoảng trắng: ").split()
list_string = []
list_numbers = []
for kt in L:
    if kt.lstrip('-').isdigit():
        list_numbers.append(int(kt))
    else:
        list_string.append(kt)
# tìm chuỗi có độ dài lớn nhất
chuoi_max = None
for chuoi in list_string:
    if chuoi_max is None or len(chuoi) > len(chuoi_max):
        chuoi_max = chuoi
print("Chuỗi có độ dài lớn nhất:", chuoi_max)
# tìm số nguyên có giá trị nhỏ nhất
so_min = None
for num in list_numbers:
    so_min = min(list_numbers)
print("Số nguyên có giá trị nhỏ nhất:", so_min)
