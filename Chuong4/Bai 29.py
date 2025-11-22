def pos_string_maxwords(ls):
    so_tu_max = 0
    vi_tri_max = -1
    for i, chuoi in enumerate(ls):
        if isinstance(chuoi, str):
            words = chuoi.split()
            if len(words) > so_tu_max:
                so_tu_max = len(words)
                vi_tri_max = i
    return vi_tri_max


n = int(input("Nhập số phần tử danh sách: "))
L = []
for k in range(n):
    gt = input(f"Nhập giá trị phần tử thứ {k + 1}: ")
    L.append(gt)
vt = pos_string_maxwords(L)
print(f"Vị trí của chuỗi có nhiều từ nhất: {vt+1}")
