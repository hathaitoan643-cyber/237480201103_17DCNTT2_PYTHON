def find_minmax_value(ds):
    min_value = min(ds)
    max_value = max(ds)
    min_index = ds.index(min_value)
    max_index = ds.index(max_value)
    return min_index, max_index


def change_minmax_pos(ds):
    min_index, max_index = find_minmax_value(ds)
    if min_index is not None and max_index is not None:
        ds[min_index], ds[max_index] = ds[max_index], ds[min_index]


L = input("Nhập dãy số nguyên, cách nhau bằng khoảng trắng: ")
number_list = [int(x) for x in L.split()]
change_minmax_pos(number_list)
print("Danh sách sau khi biến đổi:", number_list)
