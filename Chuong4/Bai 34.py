def InputDic():
    dictionary = {}
    while True:
        key_str = input("Nhập key (để dừng, hãy nhấn Enter khi key trống): ")
        if key_str == "":
            break

        value_str = input("Nhập value: ")
        dictionary[key_str] = value_str
    return dictionary


def swap_key_value(dictionary):
    swapped_dict = {}
    for key, value in dictionary.items():
        if value in swapped_dict:
            return None
        else:
            swapped_dict[value] = key
    return swapped_dict


dic = InputDic()
kq = swap_key_value(dic)

if kq is None:
    print("None")
else:
    print("Dictionary sau khi hoán đổi:", kq)
