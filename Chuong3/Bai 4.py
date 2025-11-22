def MaxPosition(list_n):
    if not list_n:
        return None
    MaxPos = 0
    MaxValue = list_n[0]
    for i in range(1, len(list_n)):
        if list_n[i] > MaxValue:
            MaxValue = list_n[i]
            MaxPos = i
    return MaxPos


list_numbers = [-1, 10, 9, -2, 3, 7, 5, 11, 6]
kt = MaxPosition(list_numbers)
if kt is not None:
    print(f"Giá trị lớn nhất trong danh sách là {list_numbers[kt]}, ở vị trí {kt+1}")
else:
    print("Danh sách rỗng.")
