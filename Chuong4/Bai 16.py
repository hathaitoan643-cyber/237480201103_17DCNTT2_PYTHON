L = input("Nhập dãy số nguyên, cách nhau bằng khoảng trắng: ")
number_list = [int(x) for x in L.split()]
x = int(input("Nhập số nguyên x: "))
list_t = []
for kt in number_list:
    dt = abs(kt - x)
    list_t.append(dt)
max_dt = max(list_t)
i_max_dt = list_t.index(max_dt)
value_xa_nhat = number_list[i_max_dt]
print(f"Giá trị trong danh sách xa {x} nhất là: ", value_xa_nhat)