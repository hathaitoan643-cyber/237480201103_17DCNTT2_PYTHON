def ShortString(list_str):
    if not list_str:
        return None
    shortstr = list_str[0]
    for i in list_str:
        if len(i) < len(shortstr):
            shortstr = i
    return shortstr


list_strings = ['jhgh', 'ftgerter', '1 v', '1fregrg4', 'sdfge']
kt = ShortString(list_strings)
if kt is not None:
    print(f"Chuỗi ngắn nhất trong danh sách là '{kt}', ở vị trí {list_strings.index(kt) + 1}")
else:
    print("Danh sách rỗng.")