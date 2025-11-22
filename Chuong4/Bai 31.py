def InputDic():
    dictionary = {}
    while True:
        key_str = input("Nhập key (để dừng, hãy nhấn Enter khi key trống): ")
        if key_str == "":
            break
        try:
            key = int(key_str)
        except ValueError:
            print("Key phải là một số nguyên. Hãy thử lại.")
            continue

        value_str = input("Nhập value: ")
        dictionary[key] = value_str

    return dictionary


def MaxKey(dictionary):
    if not dictionary:
        return None

    max_key = None
    max_value = float('-inf')

    for key, value in dictionary.items():
        if isinstance(key, int) and key > max_value:
            max_key = key
            max_value = key

    return max_key


my_dict = InputDic()
print("Dictionary đã nhập:", my_dict)

kq = MaxKey(my_dict)
if kq is not None:
    print(f"Key có giá trị lớn nhất là '{kq}'")
else:
    print("Dictionary trống hoặc không có key là số nguyên.")