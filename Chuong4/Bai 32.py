def InputDic():
    dictionary = {}
    while True:
        key_str = input("Nhập key (để dừng, hãy nhấn Enter khi key trống): ")
        if key_str == "":
            break

        value_str = input("Nhập value: ")
        dictionary[key_str] = value_str
    return dictionary


def KeyCoDoDaiLonNhat(dictionary):
    if not dictionary:
        return None

    max_key = max(dictionary, key=len)
    return max_key


my_dict = InputDic()
print("Dictionary đã nhập:", my_dict)

kq = KeyCoDoDaiLonNhat(my_dict)
if kq is not None:
    print(f"Key có độ dài lớn nhất là '{kq}'")
else:
    print("Dictionary trống hoặc không có key nào.")
