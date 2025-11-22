L = input("Nhập dãy số nguyên, cách nhau bằng khoảng trắng: ")
number_list = [int(x) for x in L.split()]
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
if a < b < len(number_list):
    sub_list = number_list[a:b]
    min_value = min(sub_list)
    print(f"Số nhỏ nhất trong danh sách từ vị trí {a} đến vị trí {b} là:", min_value)
else:
    print("a không nhỏ hơn b hoặc b vượt quá độ dài của danh sách L.")
