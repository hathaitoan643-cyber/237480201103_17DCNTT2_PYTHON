def AVGList(L, a):
    if len(L) < a:
        return None
    else:
        firstlist = L[:a]
        avg = sum(firstlist) / a
        return avg


List_numbers = [5, -1, 6, 7, -3, 8, -2]
t = 3
kt = AVGList(List_numbers, t)
if kt:
    print(f"Giá trị trung bình của {t} phần tử đầu tiên trong danh sách là: {kt}")
else:
    print("Danh sách không đủ phần tử để tính trung bình")
