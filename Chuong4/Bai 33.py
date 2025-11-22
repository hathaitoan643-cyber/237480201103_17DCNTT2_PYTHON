def InputList():
    ls = input("Nhập các chuỗi cách nhau bằng dấu phẩy: ").split(',')
    return ls


def encode_list(L):
    Dictionanry = {}
    L_mahoa = []
    count = 0
    for item in L:
        if item not in Dictionanry:
            Dictionanry[item] = count
            count += 1
        L_mahoa.append(Dictionanry[item])
    return L_mahoa, Dictionanry


List_str = InputList()
List_mahoa, dic = encode_list(List_str)

print("Dictionary mã hóa:", dic)
print("List mã hóa:", List_mahoa)
